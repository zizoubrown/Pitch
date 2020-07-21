from flask import render_template, url_for, flash, redirect
from app import app
from app.forms import RegistrationForm, LoginForm
from app.models import User, Post

pitches = [
    {
        'author': 'Abdul Aziz',
        'title':'Pitch 1',
        'content':'First Pitch content',
        'date_posted':'July 14, 2020'
    },
    {
        'author':'Anorld Swaz',
        'title':'Pitch 2',
        'content':'Second Pitch content',
        'date_posted':'July 15, 2020'
    }
]

@app.route('/')
def home():
    return render_template('home.html', pitches=pitches)

@app.route('/about')
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods= ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash('Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route('/login', methods= ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'user@pitch.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)