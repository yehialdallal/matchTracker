from app.main import bp
from flask import render_template , redirect, url_for

@bp.route('/')
def index():
    return render_template('index.html')
