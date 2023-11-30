from app.users import bp
from flask import render_template
from app.models.user import User

@bp.route('/')
def index():
    users = User.query.all()
    return render_template('users/index.html', users=users)
