"""Seed file to make sample data for pets db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()


sam = Pet(name='Sam', species='Dog', photo_url='', age='3')
whiskers = Pet(name='Whiskers', species='Cat', photo_url='https://images.unsplash.com/flagged/photo-1557427161-4701a0fa2f42?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxleHBsb3JlLWZlZWR8MXx8fGVufDB8fHx8&auto=format&fit=crop&w=800&q=60', age='3')

db.session.add_all([sam, whiskers])
db.session.commit()

