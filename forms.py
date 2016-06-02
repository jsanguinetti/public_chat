from flask.ext.wtf import Form
from wtforms import StringField, BooleanField
from wtforms.validators import DataRequired


class GreetingForm(Form):
    content = StringField('content', validators=[DataRequired()])
