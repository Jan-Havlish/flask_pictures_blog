import json

from flask_login import login_required, logout_user
from flask_login import login_user
from werkzeug.security import check_password_hash
from flask import render_template, abort, redirect, url_for, flash
from __init__ import app, db_handler, config_object, ALLOWED_EXTENSIONS, login_manager
from funcions_not_only_for_routes import try_to_load_json, SavePhotosToDbAndCopyThem, allowed_file, find_user, \
    User
from werkzeug.utils import secure_filename
import os
from flask import request


# load user by ID
@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route("/")
@app.route("/home/")
def home():
    return render_template("home.html", page="home")


@app.route("/pic/")
def redirect_to_first_pic():
    return redirect(url_for("pic", pic_num=0))


@app.route("/pic/<int:pic_num>", methods=["GET", "DELETE"])
def pic(pic_num):
    api_key = request.args.get("api_key")  # get API key

    records = db_handler.get_all()
    total_photos = len(records)
    if pic_num < 0 or pic_num >= total_photos:
        abort(404)

    name_of_img = records[pic_num]

    if request.method == "GET":
        img_src = f"/static/pic/{name_of_img}"
        img_data = db_handler.get(name_of_img)
        dictionary_of_one_img = try_to_load_json(img_data, "Error - record of this picture was not found")

        return render_template("photo.html", img_src=img_src, current_index=pic_num, total_photos=total_photos,
                               img_data=dictionary_of_one_img, page="pic")
    else:
        if api_key is None:
            abort(401)  # Unauthorized
        db_handler.delete(name_of_img)
        return json.dumps({"message": "successfully deleted"})


# Route for uploading
@app.route("/upload", methods=["GET", "POST"])
@login_required
def upload_file():
    if not config_object["enable_not_finished_functions"]:
        return '<H1> Only in unfinished version </H1> <br> <H2> For turning on this function change "config.txt"'
    if request.method == "POST":
        if "image" not in request.files:
            flash("No file part")
            return redirect(request.url)
        file = request.files["image"]
        if file.filename == "":
            flash("No selected file")
            return redirect(request.url)
        if not allowed_file(file.filename, ALLOWED_EXTENSIONS):
            flash("Invalid file extension")
            return redirect(request.url)

        # loading from the form
        description = request.form["description"]
        html_tags = request.form.get("html_tags", "")

        # creation of file name and saving
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config["UPLOAD_FOLDER"], filename))

        storing_object = SavePhotosToDbAndCopyThem(
            [{"name_of_photo": f"uploads/{filename}", "description_of_photo": description,
              "additional_html_tags": html_tags}],
            "static/pic/",
            db=db_handler.db)

        return redirect(url_for("upload_file", filename=filename))
    return render_template("upload.html", page="upload")


@app.route("/about/")
def about():
    return render_template("home.html", page="about")


@app.route("/login/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = find_user(username)

        if not user or not check_password_hash(user.password, password):
            return render_template("login.html", error=True)

        login_user(user)
        return redirect(url_for("upload_file"))
    return render_template("login.html", error=False, page="login")


@app.route("/logout/")
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.errorhandler(404)  # function for error 404 page
def page_not_found():
    return render_template("404.html"), 404
