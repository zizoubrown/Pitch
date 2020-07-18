from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import Datarequired, Length, Email, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[Datarequired(), Length(min2, max20)])
    email = StringField('Email', validators=[Datarequired(), Email()])
    password = PasswordField('Password', validators=[Datarequired()])
    confirm_password = PasswordField('Confirm Password', validators=[Datarequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Datarequired(), Email()])
    password = PasswordField('Password', validators=[Datarequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign Up')