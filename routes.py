from flask import render_template, abort, redirect, url_for
from __init__ import app, db_handler, photo_loader_instance
from funcions_for_routes import try_to_load_json, update_loader


@app.route("/")
@app.route("/home/")
def houme():
    update_loader()
    return render_template("home.html")

@app.route("/pic/")
def redirect_to_first_pic():
    return redirect(url_for('pic', pic_num=0))

@app.route("/pic/<int:pic_num>")
def pic(pic_num):

    total_photos = len(photo_loader_instance) # protection against accessing a non exiting photo
    if pic_num < 0 or pic_num >= total_photos:
        abort(404)
    name_of_img = photo_loader_instance[pic_num]
    img_src = f"/static/pic/{name_of_img}" # source of picture
    img_data = db_handler.get(name_of_img) # get record of the picture
    dictionary_of_one_img = try_to_load_json(img_data, "Error - record of this picture was not found")
    return render_template('photo.html', img_src=img_src, current_index=pic_num, total_photos=total_photos, img_data = dictionary_of_one_img)

@app.errorhandler(404) # funcion for error 404 page
def page_not_found(error):
    return render_template('404.html'), 404

@app.route("/reload_photo_loader/")
def reload_photo_loader():
    global photo_loader_instance
    photo_loader_instance.photo_names = []
    photo_loader_instance.load_photos()
    return {"value" : "updated list of photos"}