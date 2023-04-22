import json
import os
import json
import pickledb
from PIL import Image
from datetime import datetime


def try_to_load_json(JSON,
                     error_mes):  # because when showed picture which does not have a record in the db return False
    """Try to load JSON, Except - return error message."""
    true_json = {}
    try:
        true_json = json.loads(JSON)
    except TypeError:
        true_json = {"text": error_mes}
    return true_json


class save_photos_to_db_and_copy_them:
    """Save records to db, and copy photos"""

    def __init__(self, list_of_records, output_directory, db):
        self.records = list_of_records
        self.images = self.make_list_of_images()
        self.output_dir = output_directory  # "static/pic/"  # folder for images
        if db:
            self.db = db
        else:
            self.db = pickledb.load(self.DB_PATH, False)
        self.DB_PATH = "data.db"  # path to db file
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

        # print(f"processed_data: {processed_data}")

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
                # print(f"Error when copying a file {image}.")
                not_copied_images.append(image)

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


class config:
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
