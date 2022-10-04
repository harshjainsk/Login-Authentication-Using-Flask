from flask import Blueprint, render_template, request, flash, redirect, url_for

# import User from models.py
from .models import User

# to hash password using flask
from werkzeug.security import generate_password_hash, check_password_hash

# import db object
from . import db

auth = Blueprint('auth', __name__)


@auth.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("login.html", text="Logging innnnn", boolean=True)


@auth.route("/logout")
def logout():
    return "<p>Logout</p>"


@auth.route("/sign-up", methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        first_name = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        if len(email) < 4:
            flash('Email must be greater than 4 characters.', category='error')
        elif len(first_name) < 2:
            flash('First Name must be greater than 2 characters.', category='error')
        elif password1 != password2:
            flash('Passwords don\'t match', category='error')
        elif len(password1) < 7:
            flash('Password must be of at least 7 characters')
        else:
            # add user to the database
            new_user = User(email=email, first_name=first_name,
                            password=generate_password_hash(password1, method='sha256'))
            db.session.add(new_user)
            db.session.commit()

            """
                after account is created, we will redirect the user to home page
            """
            flash('Account created!', category='success')
            return redirect(url_for('views.home'))
    return render_template("sign_up.html")
