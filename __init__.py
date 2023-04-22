from flask import Flask
from db_handler import PickleDBHandler
import os
from funcions_not_only_for_routes import config

config_object = config("config.txt")

app = Flask(__name__, static_url_path="/static", )  # make app object for Flask
app.config["SECRET_KEY"] = "secret_key"
db_handler = PickleDBHandler("data.db")  # make object to easier work with PickleDB

# Získání cesty ke složce, ve které je spouštěný skript
current_dir = os.path.dirname(os.path.abspath(__file__))
# Nastavení cesty pro nahrávání souborů
app.config['UPLOAD_FOLDER'] = os.path.join(current_dir, 'uploads')

"""UPLOAD_FOLDER = 'uploads'  # Složka pro nahrávané soubory # upload settings ############ sudo chmod -R 777 /uploads
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER"""
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])
os.chmod('uploads', 0o7777)
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}  # Povolené přípony souborů
