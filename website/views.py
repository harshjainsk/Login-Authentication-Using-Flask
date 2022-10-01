from flask import Blueprint, render_template

"""
    It says that this file is the blueprint of our application 
    which simpy means it has a bunch of urls defined inside it
"""

views = Blueprint('views', __name__)


@views.route('/')
def home():
    return render_template("home.html")
