from flask import Blueprint, render_template
from flask_login import login_required, current_user
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations.view_all_bookings import view_all_bookings

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template("index.html")

@main.route('/booking')
@login_required
def booking():
    bookings = view_all_bookings(current_user.id)
    return render_template("booking.html", bookings = bookings)