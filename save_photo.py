import os
import json
import pickledb
from PIL import Image
from datetime import datetime
import click

# path to db file
DB_PATH = "data.db"


@click.command()
@click.argument('images', metavar='image', type=click.Path(exists=True), nargs=-1)
def save_photos(images):
    """Script for saving photos to blog and adding text."""
    # asking user for text for pictures, additional html and adding date
    entries = []
    for image in images:
        text = click.prompt(f'Enter text for the image "{click.style(image, fg="green")}"')
        html = ""
        html = click.prompt(f'Enter html tags for the image "{click.style(image, fg="green")}"', default="", show_default=False)
        if html is None:
            html = ""
        date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entries.append({"text": text, "html": html, "date": date})

    # copying images to a folder
    output_dir = "static/pic/"  # folder for images
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for image in images:
        try:
            with Image.open(image) as img:
                output_path = os.path.join(output_dir, os.path.basename(image))
                img.save(output_path)
                click.echo(f"File {image} was successfully copied to {output_path}")
        except:
            click.echo(f"Error when copying a file {image}.")

    # adding records to the db
    db = pickledb.load(DB_PATH, False)

    for i in range(len(images)):
        key = os.path.basename(images[i])
        value = entries[i]
        db.set(key, json.dumps(value))
        click.echo(f"The record for the {key} was successfully added to db.")

    db.dump()  # save db


if __name__ == '__main__':
    save_photos()
