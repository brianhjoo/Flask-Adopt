"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField
from wtforms.validators import InputRequired, Optional

class AddPetForm(FlaskForm):
    '''Add new pet to adoption site'''
    name = StringField(
        "Name",
        validators = [InputRequired()])

    species = StringField(
        "Species",
        validators = [InputRequired()])

    photo_url = StringField("Photo URL")

    age = SelectField(
        "Age",
        choices = [("baby", "Baby"),
                   ("young", "Young") ,
                   ("adult", "Adult"),
                   ("senior","Senior")],
        validators = [InputRequired()])

    notes = StringField("Notes")


