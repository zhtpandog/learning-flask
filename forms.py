from flask_wtf import Form 
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length

class SignupForm(Form):
	first_name = StringField('First Name', validators=[DataRequired("Please enter your first name.")])
	last_name = StringField('Last Name', validators=[DataRequired("Please enter your last name.")])
	email = StringField('Email', validators=[DataRequired("Please enter your email."), Email("Please enter valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password."), Length(min=6, message="Password should longer than 6 chars.")])
	submit = SubmitField('Sign Up')

class LoginForm(Form):
	email = StringField('Email', validators=[DataRequired("Please enter your email."), Email("Please enter valid email address.")])
	password = PasswordField('Password', validators=[DataRequired("Please enter your password."), Length(min=6, message="Password should longer than 6 chars.")])
	submit = SubmitField('Sign In')

class AddressForm(Form):
	address = StringField('Address', validators=[DataRequired("Please enter an address.")])
	submit = SubmitField('Search')