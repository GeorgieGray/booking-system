from .__init__ import app
from flask import request, jsonify
import os, sys
from datetime import datetime
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations.create_booking import create_booking
from operations.view_all_bookings import view_all_bookings
from operations.view_booking import view_booking
from operations.delete_booking import delete_booking
from operations.view_available_times import view_available_times

@app.route("/booking", methods=['GET', 'POST'])
def bookings():
    if request.method == 'GET':
        bookings = view_all_bookings(user_id=1)
        bookingsArray = []

        for booking in bookings:
            bookingsArray.append(booking.toDict())

        return jsonify(bookingsArray)

    if request.method == 'POST':
        data = request.get_json()
        date = datetime.strptime(data["date"], "%Y-%m-%d")
        create_booking(\
            group_size=data["group_size"],\
            table_id=data["table_id"],\
            time=data["time"],\
            date=date,\
            user_id=1,\
            note=data["note"],\
        )
        return "Booking created successfully"

@app.route("/booking/<id>", methods=['GET', 'DELETE'])
def booking(id):
    if request.method == 'GET':
        booking = view_booking(id=id, user_id=1)
        return jsonify(booking.toDict())
    if request.method == 'DELETE':
        delete_booking(id=id, user_id=1)
        return f"booking {id} deleted successfully"


@app.route("/booking/time", methods=['POST'])
def time():
    if request.method == 'POST':
        data = request.get_json()
        date = datetime.strptime(data["booking_day"], "%Y-%m-%d")
        times = view_available_times(\
            restaurant_id=data["restaurant_id"],\
            party_size=data["party_size"],\
            booking_day=date\
        )
        return jsonify(times)