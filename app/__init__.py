from flask import Flask
from flask_login import LoginManager
import os, sys
from .api import api as api_blueprint
from .view.auth import auth as auth_blueprint
from .view.main import main as main_blueprint
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from models.user import User
from db import session
from dotenv import load_dotenv

load_dotenv()
SECRET_KEY = os.getenv('SECRET_KEY')

template_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
template_folder = os.path.join(template_folder, 'app')
template_folder = os.path.join(template_folder, 'templates')

static_folder = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
static_folder = os.path.join(static_folder, 'static')

app = Flask(__name__, template_folder=template_folder, static_folder=static_folder, static_url_path="/static")

app.config['SECRET_KEY'] = SECRET_KEY

app.register_blueprint(api_blueprint)
app.register_blueprint(auth_blueprint)
app.register_blueprint(main_blueprint)

login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    return session.query(User).get(user_id)
