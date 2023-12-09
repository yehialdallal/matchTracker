from app.auth import bp
from flask import render_template, flash , redirect , url_for
from app.models.user import User
from flask_login import login_required , current_user , logout_user



@bp.route('/')
@login_required
def index():
    return render_template('auth/index.html',name=current_user.name)

@bp.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out.')
    return redirect(url_for('main.index'))

@bp.route('/login')
@login_required
def login():
    return render_template('auth/index.html',name=current_user.name)
    #return render_template('auth/index.html')

@bp.route('/signup')
def signup():
    return 'signup completed'
    #return render_template('index.html')
