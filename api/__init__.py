from flask import Flask
app = Flask(__name__)

from .booking import *
from .user import *