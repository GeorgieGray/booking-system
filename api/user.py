from .__init__ import app
from flask import request

@app.route("/user/login", methods=['POST'])
def login():
   if request.method == 'POST':
        return "user login"

@app.route("/user/logout", methods=['POST'])
def logout():
   if request.method == 'POST':
        return "user logout"


@app.route("/user/password", methods=['PUT'])
def password():
   if request.method == 'PUT':
        return "change password"

@app.route("/user/email", methods=['PUT'])
def email():
   if request.method == 'PUT':
        return "change email"

