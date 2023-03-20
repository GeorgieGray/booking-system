from flask import request, jsonify, flash, redirect, url_for
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash
import os, sys
from .__init__ import api
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from operations.check_email_in_use import check_email_in_use
from operations.create_user import create_user
from operations.get_user import get_user
from helpers.validation import is_valid_email, length_between

@api.route("/user/login", methods=['POST'])
def login():
   if request.method == 'POST':
      json = request.get_json()

      email = json['email'] if 'email' in json else ''
      password = json['password'] if 'password' in json else ''
      remember = json['remember'] if 'remember' in json else False

      user = get_user(email)

      if not user or not check_password_hash(user.password, password):
         return "wrong credentials", 401
      
      login_user(user, remember=remember)
      return "success", 200

@api.route("/user/register", methods=['POST'])
def register():
   if request.method == 'POST':
      json = request.get_json()

      if not is_valid_email(json['email']):
         return "email not valid", 400

      if not length_between(json['first-name'], 3, 15):
         return "first-name must be between 3 and 15 characters", 400

      if not length_between(json['last-name'], 3, 15):
         return "last-name must be between 3 and 15 characters", 400

      if not length_between(json['password'], 3, 15):
         return "password must be between 3 and 15 characters", 400
      
      if check_email_in_use(json['email']):
         return "email already in use", 400

      password = generate_password_hash(password=json['password'], method="sha256")

      user = create_user(
         email = json['email'],\
         password = password,\
         first_name=json['first-name'],\
         last_name=json['last-name']\
      )

      login_user(user)

      response = {
         'user_id': user.id
      }

      return jsonify(response), 200
