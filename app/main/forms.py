from flask_wtf import FlaskForm
from wtforms import (StringField, SubmitField)
from wtforms.validators import InputRequired

class NameForm(FlaskForm):
    name = StringField("What is your name?", validators=[InputRequired()])
    submit = SubmitField('Submit')