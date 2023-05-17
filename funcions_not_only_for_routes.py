import os
import json
import pickledb
from PIL import Image
from datetime import datetime
from password_and_user import users
from flask_login import UserMixin
from typing import Dict, Any, List


def try_to_load_json(JSON,
                     error_mes):  # because when showed picture which does not have a record in the db return False
    """Try to load JSON, Except - return error message."""
    true_json = {}
    try:
        true_json = json.loads(JSON)
    except TypeError:
        true_json = {"text": error_mes}
    return true_json


class SavePhotosToDbAndCopyThem:  # save_photos_to_db_and_copy_them
    """Save records to db, and copy photos"""

    def __init__(self, list_of_records, output_directory, db):
        self.records = list_of_records
        self.images = self.make_list_of_images()
        self.output_dir = output_directory  # "static/pic/"  # folder for images
        if db:
            self.db = db
        else:
            self.DB_PATH = "data.db"  # path to db file
            self.db = pickledb.load(self.DB_PATH, False)
        self.save_data()

    def make_list_of_images(self):
        img_list = []
        for one_record in self.records:
            one_img_name = one_record["name_of_photo"]
            img_list.append(one_img_name)

        return img_list

    def save_data(self):
        processed_data = []

        for one_record in self.records:
            text = one_record["description_of_photo"]
            html = one_record["additional_html_tags"]
            date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            processed_data.append({"text": text, "html": html, "date": date})

        # copying images to a folder
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

        not_copied_images = []
        for image in self.images:
            try:
                with Image.open(image) as img:
                    output_path = os.path.join(self.output_dir, os.path.basename(image))
                    img.save(output_path)
                    # print(f"File {image} was successfully copied to {output_path}")
            except:
                not_copied_images.append(image)
                # print(f"Error when copying a file {image}.")

        # adding correct records to the db
        db = self.db

        for i in range(len(self.images)):
            if self.images[i] in not_copied_images:
                continue
            key = os.path.basename(self.images[i])
            value = processed_data[i]
            db.set(key, json.dumps(value))
            # print(f"The record for the {key} was successfully added to db.")

        db.dump()  # save db


class LoadConfig:
    def __init__(self, name_of_conf_file):
        self.conf_file = name_of_conf_file
        self.config_JSON = {}
        self.load()

    def load(self):
        with open(self.conf_file) as file:
            json_to_load = file.readline()  # json.loads()
            self.config_JSON = json.loads(json_to_load)

    def __getitem__(self, key):
        return self.config_JSON[key]


# control extensions
def allowed_file(filename, EXTENSIONS):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in EXTENSIONS


class User(UserMixin):
    def __init__(self, username):
        self.id = username
        self.password = users.get(username).get('password')
        self.username = username

    def __repr__(self):
        return f'<User {self.username}>'


# find user
def find_user(username):
    if username in users:
        return User(username)
    return None

class WorkWithDBData: # use this to replace funcions under
    def __init__(self, db_handler_instance: Any):
        self.db_handler = db_handler_instance
        #print(f"DB handler: {self.db_handler}")
        self.db_list = []
        self.updadate_db_list()
        self.leght_of_db = len(self.db_list)

    def updadate_db_list(self):
        self.db_list = self.db_handler.get_all()

    def get_all_records_data_as_list(self) -> List[Dict[str, Any]]:
        all_pictures = self.db_handler.get_all()
        data_records = []
        for pic in all_pictures:
            data_records.append(self.db_handler.get(pic))
        return data_records
    
    def get_all_titles_of_all_records(self):
        all_data_list = self.get_all_records_data_as_list()
        titles = []
        #print(all_data_list)
        for data in all_data_list:
            data = json.loads(data)
            #print(f"------------ \n Data: {data} \n Text {data['text']} ------------")
            titles.append(data["text"])
        return titles  
    def titles_and_num_of_posts(self):
        list_of_articles_titles_with_their_num = []
        for i, title in enumerate(self.get_all_titles_of_all_records()):
            list_of_articles_titles_with_their_num.append({"title" : title, "number" : i})                
            #print(f"{title} - {i}")
        return(list_of_articles_titles_with_their_num)

