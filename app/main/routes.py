from app.main import bp
from flask import render_template , redirect, url_for , request , flash
from app.models.forms import LoginForm , SignupForm

@bp.route('/', methods=['GET','POST'])
def index():
    #return render_template('index.html')
    login_form = LoginForm()
    signup_form = SignupForm()

    if request.method == 'POST':
        if login_form.submit1.data and login_form.validate():
            return redirect(url_for('auth.login'))
            # Handle login logic
            #email = login_form.email.data
            #password = login_form.password.data
            # Perform authentication logic
            #return 'Login successful!'  # Redirect or display success message
        #elif request.form['form_type'] == 'signup':
        #if request.form['action'] == 'login':
        
        elif signup_form.submit2.data and signup_form.validate() :
            return redirect(url_for('auth.signup'))
                #return 'signed up succesully'
            #return redirect(url_for('auth.signup'))
        
            # Handle signup logic
            #name = signup_form.name.data
            #email = signup_form.email.data
            #password = signup_form.password.data
            # Perform signup logic
            #signup_form.name.errors = []
            # Redirect or display success message
        
    return render_template('index.html', login_form=login_form, signup_form=signup_form)
    #return 'none submitted'



##########################
@bp.route('/ff', methods=['GET', 'POST'])
def login_signup():
    login_form = LoginForm()
    signup_form = SignupForm()

    if request.method == 'POST':
        if request.form['action'] == 'login':  # Check which button was clicked
            form = login_form
            if form.validate_on_submit():
                # Handle login logic
                username = form.username.data
                password = form.password.data
                # Perform authentication logic
                return 'Login successful!'  # Redirect or display success message

        elif request.form['action'] == 'signup':
            form = signup_form
            if form.validate_on_submit():
                # Handle signup logic
                username = form.username.data
                email = form.email.data
                password = form.password.data
                # Perform signup logic
                return 'Signup successful!'  # Redirect or display success message

    return render_template('index.html', login_form=login_form, signup_form=signup_form)

