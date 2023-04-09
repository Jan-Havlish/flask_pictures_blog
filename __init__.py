from flask import Flask
from db_handler import PickleDBHandler
from photos_procesing import photo_loader
from funcions_for_routes import return_dir_of_pictures

app = Flask(__name__, static_url_path="/static", ) # make app object for Flask
app.config["SECRET_KEY"] = "secret_key"
db_handler = PickleDBHandler("data.db") # make object to easier work with PickleDB
pic_dir = return_dir_of_pictures() # found where pictures are stored
photo_loader_instance = photo_loader(pic_dir)