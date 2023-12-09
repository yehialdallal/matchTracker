from flask import render_template , redirect, url_for , request ,flash , session, \
    current_app, request , abort
from flask_login import login_user , current_user
from werkzeug.security import generate_password_hash, check_password_hash

from urllib.parse import urlencode
import os
import secrets
from dotenv import load_dotenv
import requests

from app.main import bp
from app.models.forms import LoginForm , SignupForm
from app.extensions import db
from app.models.user import User
from app import login_manager

load_dotenv()

@bp.route('/', methods=['GET','POST'])
def index():
    if not current_user.is_anonymous:
        return redirect(url_for('auth.index'))

    login_form = LoginForm()
    signup_form = SignupForm()
    
    if request.method == 'POST':
        if login_form.submit1.data and login_form.validate():
            email = login_form.login_email.data
            password = login_form.password1.data
            remember = login_form.remember_me.data
            user = User.query.filter_by(email=email).first()
            
            #invalid
            if not user or not check_password_hash(user.password, password):
                flash('Please check your login details and try again.')
                return redirect(url_for('main.index')) # if the user doesn't exist or password is wrong, reload the page
            
            #valid
            login_user(user, remember=remember)
            return redirect(url_for('auth.login'))
            
        elif signup_form.submit2.data and signup_form.validate() :
            user = User.query.filter_by(email=signup_form.signup_email.data).first()
            if user:
                flash('Email address already exists')
                return redirect(url_for('main.index'))
            else:
                user = User(
                    name=signup_form.name.data,
                    email=signup_form.signup_email.data,
                    password=generate_password_hash(signup_form.password2.data, method='sha256'),
                    mobile=signup_form.mobile.data
                )
                db.session.add(user)
                db.session.commit()
                flash(f"{signup_form.name.data} uploaded!", "success")
                return redirect(url_for('auth.signup'))
                
    return render_template('index.html', login_form=login_form, signup_form=signup_form )
    #return 'none submitted'



##########################

@bp.route('/users', methods=['GET'])
def getUsers():
    users = User.query.all()
    return render_template('users.html',users=users)


####################################

@bp.route('/authorize/<provider>')
def oauth2_authorize(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('auth.index'))

    provider_data = current_app.config['OAUTH2_PROVIDERS'].get(provider)
    if provider_data is None:
        abort(404)

    # generate a random string for the state parameter
    session['oauth2_state'] = secrets.token_urlsafe(16)

    # create a query string with all the OAuth2 parameters
    qs = urlencode({
        'client_id': provider_data['client_id'],
        'redirect_uri': url_for('main.oauth2_callback', provider=provider,
                                _external=True),
        'response_type': 'code',
        'scope': ' '.join(provider_data['scopes']),
        'state': session['oauth2_state'],
    })

    # redirect the user to the OAuth2 provider authorization URL
    return redirect(provider_data['authorize_url'] + '?' + qs)


@bp.route('/callback/<provider>')
def oauth2_callback(provider):
    if not current_user.is_anonymous:
        return redirect(url_for('auth.index'))

    provider_data = current_app.config['OAUTH2_PROVIDERS'].get(provider)
    if provider_data is None:
        abort(404)

    # if there was an authentication error, flash the error messages and exit
    if 'error' in request.args:
        for k, v in request.args.items():
            if k.startswith('error'):
                flash(f'{k}: {v}')
        return redirect(url_for('main.index'))

    # make sure that the state parameter matches the one we created in the
    # authorization request
    if request.args['state'] != session.get('oauth2_state'):
        abort(401)

    # make sure that the authorization code is present
    if 'code' not in request.args:
        abort(401)

    # exchange the authorization code for an access token
    response = requests.post(provider_data['token_url'], data={
        'client_id': provider_data['client_id'],
        'client_secret': provider_data['client_secret'],
        'code': request.args['code'],
        'grant_type': 'authorization_code',
        'redirect_uri': url_for('main.oauth2_callback', provider=provider,
                                _external=True),
    }, headers={'Accept': 'application/json'})
    if response.status_code != 200:
        abort(401)
    oauth2_token = response.json().get('access_token')
    if not oauth2_token:
        abort(401)

    # use the access token to get the user's email address
    response = requests.get(provider_data['userinfo']['url'], headers={
        'Authorization': 'Bearer ' + oauth2_token,
        'Accept': 'application/json',
    })
    if response.status_code != 200:
        abort(401)
    email = provider_data['userinfo']['email'](response.json())

    # find or create the user in the database
    user = User.query.filter_by(email=email).first()
    if user is None:
        user = User(email=email, name=email.split('@')[0])
        db.session.add(user)
        db.session.commit()

    # log the user in
    login_user(user)
    return redirect(url_for('auth.index'))


