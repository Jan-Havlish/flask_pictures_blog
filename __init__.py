from flask import Flask
from db_handler import PickleDBHandler

app = Flask(__name__, static_url_path="/static", )  # make app object for Flask
app.config["SECRET_KEY"] = "secret_key"
db_handler = PickleDBHandler("data.db")  # make object to easier work with PickleDB
