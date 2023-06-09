"""Flask app for adopt app."""

from flask import Flask, request, redirect, render_template, flash

from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db
from forms import AddPetForm, EditPetForm

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)


@app.get("/")
def load_homepage():
    """Display Homepage of Pets"""

    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)


@app.route("/add", methods=["GET", "POST"])
def add_pet():
    """Show add pet form & add a pet to the database"""

    form = AddPetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name,
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes
        )

        db.session.add(new_pet)
        db.session.commit()
#TODO: add flash msg to base.html
        flash(f'Added {name} to pets database!')
        return redirect('/')
    else:
        return render_template('add_pet_form.html', form=form)


@app.route('/<int:pet_id>', methods=['GET', 'POST'])
def edit_pet(pet_id):
    """Edit a pet"""

    pet = Pet.query.get(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data

        db.session.commit()
        flash(f"{pet.name}'s record has been updated")

        return redirect(f"/{pet_id}")
    else:
        return render_template("pet_details.html", form=form, pet=pet)
