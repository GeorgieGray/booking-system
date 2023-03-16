from flask import Flask
import os
template_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_folder = os.path.join(template_folder, 'app')
template_folder = os.path.join(template_folder, 'templates')
print(template_folder)
app = Flask(__name__, template_folder=template_folder)

from .api import api as api_blueprint
from .view.auth import auth as auth_blueprint
from .view.main import main as main_blueprint

app.register_blueprint(api_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)