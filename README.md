# Simple blog for sharing images written with Flask

This project is a simple Blog for sharing images.

## Features

- Each image can have a text description and additional html tags. 
  - The date of publication is also displayed.
- Images can be added to the blog with use of save_photo.py script. 
  - This script need args.
  - In this time this script can only work with images stored in same folder as script.
    Example of using the script: "python3 save_photo.py a.jpg b.png c.jpg
    - This time the blog can display only .jpg or .png photos but is easy to add 
support for photos of other formats.
  - Pictures added to the "pic" folder without usage of this script will be displayed 
without additional information and with an error message.
  - Pictures removed from the "pic" folder will no longer be displayed.

## Using of the *save_photo.py* script

- This script is only one right way to save pub images to blog in this time.
- Basics about this script is in the previous article.
- After you run this script with args you will be asked firstly for some text for
image and for additional html tags (unnecessary)

## License

- This work is under MIT license.
- What is [MIT license](https://en.wikipedia.org/wiki/MIT_License  "About MIT license on wikipedia.org").

## Acknowledgments

Thanks to ChatGPT in particular for "explaining error messages", examples of working
with some libraries, and for the JS code, as I needed some JS but haven't learned it 
much yet.

## I almost forgot

This app contain 4 example files (a.jpg, b.jpg, c.jpg, data.db) and folder pic 
(stored in static). You can remove this files when you like (before you add own
records).

### To do

- More about thing that I like to add is in TO_DO.md

***

**I hope this project has been helpful to you.**

Jan Havliš 