from flask import request
import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from app.__init__ import app

@app.route("/api/user/login", methods=['POST'])
def login():
   if request.method == 'POST':
        return "user login"

@app.route("/api/user/logout", methods=['POST'])
def logout():
   if request.method == 'POST':
        return "user logout"


@app.route("/api/user/password", methods=['PUT'])
def password():
   if request.method == 'PUT':
        return "change password"

@app.route("/api/user/email", methods=['PUT'])
def email():
   if request.method == 'PUT':
        return "change email"

