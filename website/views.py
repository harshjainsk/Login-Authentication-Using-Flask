from flask import Blueprint, render_template, request, flash
from flask_login import login_required, current_user
from .models import Note
from . import db

"""
    It says that this file is the blueprint of our application 
    which simpy means it has a bunch of urls defined inside it
"""

views = Blueprint('views', __name__)

"""
    Unless the user is not logged-in, they should not access the
    home page
"""


@views.route('/', methods=['POST', 'GET'])
@login_required
def home():

    if request.method == 'POST':
        note = request.form.get('note')

        if len(note) < 1:
            flash('Note is too short', category='error')
        else:
            new_note = Note(data=note, user_id=current_user.id)
            db.session.add(new_note)
            db.session.commit()
            flash('Note added successfully!', category='success')
    return render_template("home.html", user=current_user)
