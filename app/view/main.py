from flask import Blueprint, render_template
from flask_login import login_required

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/booking')
@login_required
def booking():
    return render_template("booking.html")