from flask import Blueprint, render_template
from flask_login import login_required, current_user

"""
    It says that this file is the blueprint of our application 
    which simpy means it has a bunch of urls defined inside it
"""

views = Blueprint('views', __name__)

"""
    Unless the user is not logged-in, they should not access the
    home page
"""


@views.route('/')
@login_required
def home():
    return render_template("home.html")
