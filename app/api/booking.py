from flask import request, jsonify
from flask_login import login_required, current_user
import os, sys
from datetime import datetime
from .__init__ import api
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from operations.create_booking import create_booking
from operations.view_all_bookings import view_all_bookings
from operations.view_booking import view_booking
from operations.delete_booking import delete_booking
from operations.view_available_times import view_available_times

@api.route("/booking", methods=['GET', 'POST'])
@login_required
def bookings():
    if request.method == 'GET':
        bookings = view_all_bookings(user_id=current_user.id)
        bookingsArray = []

        for booking in bookings:
            dict = booking.toDict()
            dict['table'] = booking.table.toDict()
            bookingsArray.append(dict)


        return jsonify(bookingsArray)

    if request.method == 'POST':
        data = request.get_json()
        date = datetime.strptime(data["date"], "%Y-%m-%d")
        result = view_available_times(\
            restaurant_id=data["restaurant_id"],\
            group_size=data["group_size"],\
            booking_day=date\
        )
        match = None
        for time, table in result["available_time_and_table_pairs"]:
            if (time == data["time"]):
                match = table
                break

        if (match == None):
            return "No available table for provided time", 400
        
        booking = create_booking(\
            group_size=data["group_size"],\
            table_id=match["id"],\
            time=data["time"],\
            date=date,\
            user_id=current_user.id,\
            note="",\
        )
        return booking.toDict(), 200

@api.route("/booking/<id>", methods=['GET', 'DELETE'])
@login_required
def booking(id):
    if request.method == 'GET':
        booking = view_booking(id=id, user_id=current_user.id)
        dict = booking.toDict()
        dict['table'] = booking.table.toDict()
        return jsonify(dict), 200
    if request.method == 'DELETE':
        success = delete_booking(id=id, user_id=current_user.id)
        if not success:
            return "booking delete failed", 400
        return f"booking {id} deleted successfully", 200


@api.route("/booking/time", methods=['POST'])
def time():
    if request.method == 'POST':
        data = request.get_json()
        date = datetime.strptime(data["booking_day"], "%Y-%m-%d")
        result = view_available_times(\
            restaurant_id=data["restaurant_id"],\
            group_size=data["group_size"],\
            booking_day=date\
        )

        return jsonify(result["available_times"]), 200