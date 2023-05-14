from werkzeug.security import generate_password_hash

password = generate_password_hash("blog")  # password
users = {"user": {"password": password}}  # user name
