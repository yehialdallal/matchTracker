from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField , HiddenField
from wtforms.validators import DataRequired, Email, EqualTo

class LoginForm(FlaskForm):
    login_email = StringField('Email', validators=[DataRequired(),Email()])
    password1 = PasswordField('Password', validators=[DataRequired()])
    submit1 = SubmitField('login')
    #form_type = HiddenField('login')

class SignupForm(FlaskForm):
    name = StringField('Username', validators=[DataRequired()])
    signup_email = StringField('Email', validators=[DataRequired(),Email()])
    mobile = StringField('Mobile Number', validators=[DataRequired()])
    password2 = PasswordField('Password', validators=[DataRequired()])
    #confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit2 = SubmitField('signup')
    #form_type = HiddenField('signup')
