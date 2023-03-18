"""Forms for adopt app."""

from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, RadioField, TextAreaField
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

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])

    age = SelectField(
        "Age",
        choices = [("baby", "Baby"),
                   ("young", "Young") ,
                   ("adult", "Adult"),
                   ("senior","Senior")],
        validators = [InputRequired()])

    notes = TextAreaField("Notes", validators = [Optional()] )


class EditPetForm(FlaskForm):
    '''Edit pet'''

    photo_url = StringField("Photo URL", validators=[URL(), Optional()])

    notes = TextAreaField("Notes")

    available = RadioField(
            'Available',
            choices=[("True", "Yes"), ("", "No")],
            coerce=bool
    )

    #note: booleanfield requires optional to not be checked


