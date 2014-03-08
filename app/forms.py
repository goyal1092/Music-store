from flask.ext.wtf import Form
from wtforms import TextField,PasswordField
from wtforms.validators import Required, Email

class UserLoginForm(Form):
    email = TextField('Email', validators=[Required(), Email('Please enter a valid email.')])
    password = PasswordField('Password', validators=[Required()])



