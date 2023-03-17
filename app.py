"""Flask app for adopt app."""

from flask import Flask, request, redirect, render_template

from flask_debugtoolbar import DebugToolbarExtension

from models import connect_db, Pet, db

app = Flask(__name__)

app.config['SECRET_KEY'] = "secret"

app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///adopt"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

connect_db(app)

# Having the Debug Toolbar show redirects explicitly is often useful;
# however, if you want to turn it off, you can uncomment this line:
#
# app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

toolbar = DebugToolbarExtension(app)

@app.get("/")
def load_homepage():
    pets = Pet.query.all()

    return render_template("homepage.html", pets=pets)

@app.route("/add", method=["GET", "POST"])
def add_pet():
    form =
