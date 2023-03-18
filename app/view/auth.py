from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user, logout_user

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    if current_user.is_authenticated:
        print("already logged in")
        return redirect(url_for("main.booking"))

    return render_template("login.html")

@auth.route('/signup')
def signup():
    return render_template("signup.html")

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))