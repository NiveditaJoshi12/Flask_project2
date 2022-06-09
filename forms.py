from django.forms import EmailField
from flask_wtf import Form
from wtforms.fields import  IntegerField, TextAreaField, SubmitField, RadioField, SelectField  
from wtforms import validators, ValidationError  

class ContactForm(Form):
    name = TextAreaField('Candidate Name',[validators.Required("Please enter your name.")])
    gender=RadioField('Gender', choices=[('M','Male'),('F','Female')])
    address = TextAreaField('Address')
    email = TextAreaField("Email",[validators.Required("Please enter your name.")])
    age = IntegerField('Age')
    language = SelectField('Programming Languages',choices=[('java','Java'),('py','Python')])
    submit = SubmitField('Submit')

