from app.main import bp
from flask import render_template , redirect, url_for , request ,flash
from app.models.forms import LoginForm , SignupForm
from app.extensions import db
from app.models.user import User
from app import login_manager
from werkzeug.security import generate_password_hash, check_password_hash

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@bp.route('/', methods=['GET','POST'])
def index():
    login_form = LoginForm()
    signup_form = SignupForm()

    if request.method == 'POST':
        if login_form.submit1.data and login_form.validate():
            email = login_form.login_email.data
            password = login_form.password1.data
            #remember = True if request.form.get('remember') else False
            user = User.query.filter_by(email=email).first()
            if not user or not check_password_hash(user.password, password):
                flash('Please check your login details and try again.')
                return redirect(url_for('main.index')) # if the user doesn't exist or password is wrong, reload the page

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

