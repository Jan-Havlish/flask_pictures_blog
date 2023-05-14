from flask import Flask
from db_handler import PickleDBHandler
import os
from funcions_not_only_for_routes import LoadConfig
from flask_login import LoginManager

config_object = LoadConfig("config.txt")

app = Flask(__name__, static_url_path="/static", )  # make app object for Flask
app.config["SECRET_KEY"] = "secret_key"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

db_handler = PickleDBHandler("data.db")  # make object to easier work with PickleDB

# find where is running this script
current_dir = os.path.dirname(os.path.abspath(__file__))
# set upload folder
app.config["UPLOAD_FOLDER"] = os.path.join(current_dir, "uploads")

if not os.path.exists(app.config["UPLOAD_FOLDER"]):
    os.makedirs(app.config["UPLOAD_FOLDER"])
os.chmod("uploads", 0o7777)

ALLOWED_EXTENSIONS = {"txt", "pdf", "png", "jpg", "jpeg", "gif"}  # allowed extensions
