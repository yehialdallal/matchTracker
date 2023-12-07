from app.auth import bp
from flask import render_template , redirect, url_for , request , flash
from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash
from app.extensions import db

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('auth/index.html', users=users)

@bp.route('/logout')
def logout():
    return render_template('index.html')

@bp.route('/login')
def login():
    return 'login comoleted'
    #return render_template('auth/index.html')

@bp.route('/signup')
def signup():
    return 'signup completed'
    #return render_template('index.html')

@bp.route('/signup', methods=['POST'])
def signup_post():
    # code to validate and add user to database goes here
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()
    if user:
        # if a user is found, we want to redirect back to signup page so user can try again
        flash('Email address already exists')
        return redirect(url_for('auth.routes.signup'))
    # create a new user with the form data. Hash the password so the plaintext version isn't saved.
    new_user = User(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    # add the new user to the database
    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.routes.login')) #check thiss!
