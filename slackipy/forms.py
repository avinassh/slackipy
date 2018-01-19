from flask_wtf import Form
from wtforms import validators
from wtforms.fields.html5 import EmailField


class InviteForm(Form):
    email = EmailField('Email Address',
                       [validators.DataRequired(), validators.Email()])
