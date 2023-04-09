import argparse
import os
import json
import pickledb
from PIL import Image
from datetime import datetime

# path to db file
DB_PATH = "data.db"

# load args
parser = argparse.ArgumentParser(description='Script for saving photos to blog and adding text.')
parser.add_argument('images', metavar='image', type=str, nargs='+',
                    help='name of pictures to save')
args = parser.parse_args()

# asking user for text for pictures, additional html and adding date
entries = []
for image in args.images:
    text = input(f'Enter text for the image "{image}": ')
    html = input(f'Enter html tags for the image "{image}": ')
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entries.append({"text": text, "html": html, "date": date})

# copying images to a folder
output_dir = "static/pic/" # folder for images
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for image in args.images:
    try:
        with Image.open(image) as img:
            output_path = os.path.join(output_dir, os.path.basename(image))
            img.save(output_path)
            print(f"File {image}  was successfully copied to {output_path}")
    except:
        print(f"Error when copying a file {image}.")

# adding records to the db
db = pickledb.load(DB_PATH, False)

for i in range(len(args.images)):
    key = os.path.basename(args.images[i])
    value = entries[i]
    db.set(key, json.dumps(value))
    print(f"The record for the {key} was successfully added to db.")

db.dump() # save db