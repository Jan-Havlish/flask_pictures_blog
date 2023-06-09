# Simple blog for sharing images written with Flask

This project is a simple Blog for sharing images.

## Features

- Each image can have a text description and additional html tags. 
  - The date of publication is also displayed.
- Images can be added to the blog with use of save_photo.py script. 
  - This script need args.
  - In this time this script can only work with images stored in same folder as script.
    Example of using the script: "python3 save_photo.py a.jpg b.png c.jpg d.bmp
    - This time the blog can display any standard types of photos (.jpg, .png, .bmp and 
more)
- Or after log in in web interface
  - Default username: "blog"
  - Default password: "flask"
  - changeable in "password_and_user.py"
## Install
1) Copy projects file to directory that you want
2)  **Optional** - Create and setup virtual environment
3) In the main folder of this project run: pip install -r requirements.txt in a terminal
4) Change what do you want
5) Run the run.py script: python run.py

## Using of the *save_photo.py* script

- This script is only one right way to save pub images to blog in this time.
- Basics about this script is in the previous article.
- After you run this script with args you will be asked firstly for some text for
image and for additional html tags (unnecessary)

## License

- This work is under MIT license.
- What is [MIT license](https://en.wikipedia.org/wiki/MIT_License  "About MIT license on wikipedia.org").

## Acknowledgments

- Thanks to Bootstrap for their CSS

- Thanks to ChatGPT in particular for "explaining error messages", examples of working
with some libraries, and for the JS code, as I needed some JS but haven't learned it 
much yet.

## I almost forgot

This app contain 5 example files (a.jpg, b.jpg, c.jpg, d.bmp, data.db) and folder pic 
(stored in static). You can remove this files when you like (before you add own
records).

### To do

- More about thing that I like to add is in TO_DO.md

***

**I hope this project has been helpful to you.**

Jan Havliš 