from .__init__ import app
from flask import request

@app.route("/booking", methods=['GET', 'POST'])
def bookings():
    if request.method == 'GET':
        return "get_all_bookings"
    if request.method == 'POST':
        return "create_a_booking"

@app.route("/booking/<id>", methods=['GET', 'DELETE'])
def booking(id):
    if request.method == 'GET':
        return f"retrieve_booking {id}"
    if request.method == 'DELETE':
        return f"delete_a_booking {id}"
   