from app.auth import bp
from flask import render_template
from app.models.user import User



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
