import click
from funcions_not_only_for_routes import save_photos_to_db_and_copy_them


@click.command()
@click.argument('images', metavar='image', type=click.Path(exists=True), nargs=-1)
def save_photos(images):
    """Script for saving photos to blog and adding text."""
    # asking user for text for pictures, additional html and adding date
    entries = []
    for image in images:
        text = click.prompt(f'Enter text for the image "{click.style(image, fg="green")}"')
        html = ""
        html = click.prompt(f'Enter html tags for the image "{click.style(image, fg="green")}"', default="",
                            show_default=False)
        if html is None:
            html = ""
        entries.append({"name_of_photo": image, "description_of_photo": text, "additional_html_tags": html})
    print(f"from input: {entries}")

    storing_object = save_photos_to_db_and_copy_them(entries, "static/pic/")

    print("Done")

# storing_object = save_photos_to_db_and_copy_them({"name_of_photo": image, "description_of_photo": text, "additional_html_tags": html}, "static/pic/")
if __name__ == '__main__':
    save_photos()
