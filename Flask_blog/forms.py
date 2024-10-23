from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,BooleanField,EmailField
from wtforms.validators import DataRequired, Length,EqualTo

class RegistrationForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired(),Length(min=2,max=20)])
    email =EmailField('Email',validators=[DataRequired()])
    password=StringField('Password', validators=[DataRequired()])
    confirm_password=StringField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

class LogInForm(FlaskForm):
    email =EmailField('Email',validators=[DataRequired()])
    password=StringField('Password', validators=[DataRequired()])
    remember=BooleanField('Remember Me')
    submit = SubmitField('Login')
    
