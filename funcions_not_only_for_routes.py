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

    def __init__(self, list_of_records, output_directory):
        self.records = list_of_records
        self.images = self.make_list_of_images()
        self.output_dir = output_directory  # "static/pic/"  # folder for images
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
        db = pickledb.load(self.DB_PATH, False)

        for i in range(len(self.images)):
            if self.images[i] in not_copied_images:
                continue
            key = os.path.basename(self.images[i])
            value = processed_data[i]
            db.set(key, json.dumps(value))
            # print(f"The record for the {key} was successfully added to db.")

        db.dump()  # save db
