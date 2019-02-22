from flask_wtf import FlaskForm

from wtforms import StringField

from wtforms.validators import DataRequired, Email

class ContactForm(FlaskForm):

    name = StringField('full_name', validators=[DataRequired()])

    email = StringField('email', validators=[DataRequired(), Email()])
    
    subject = StringField('subject', validators=[DataRequired()])
    
    message = StringField('message', validators=[DataRequired()])