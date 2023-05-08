from werkzeug.security import generate_password_hash

password = generate_password_hash("blog") # pasword
users = {"user": {"password": password}} # user name
