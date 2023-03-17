"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, SelectField, BooleanField
from wtforms.validators import InputRequired, Optional, AnyOf, URL

class AddPetForm(FlaskForm):
    '''Add new pet to adoption site'''
    name = StringField(
        "Name",
        validators = [InputRequired()])

    species = StringField(
        "Species",
        validators = [InputRequired(),
                        AnyOf(['cat', 'dog', 'porcupine'])
                    ])

    photo_url = StringField("Photo URL", validators=[URL()])

    age = SelectField(
        "Age",
        choices = [("baby", "Baby"),
                   ("young", "Young") ,
                   ("adult", "Adult"),
                   ("senior","Senior")],
        validators = [InputRequired()])

    notes = StringField("Notes")


class EditPetForm(FlaskForm):
    '''Edit pet'''

    photo_url = StringField("Photo URL", validators=[URL()])

    notes = StringField("Notes")

    available = BooleanField(
            'Available',
            default='checked',
            validators=[InputRequired()]
    )


