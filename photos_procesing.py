import os
class photo_loader:
    """Class for loading images"""
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.photo_names = []
        self.load_photos()

    def load_photos(self):
        # Get a list of file names in a directory
        file_names = os.listdir(self.folder_path)

        # Sort file names by the numeric string at the beginning of the name (if any)
        sorted_names = sorted(file_names, key=lambda x: (
        int(''.join(filter(str.isdigit, x))) if x[0].isdigit() else float('inf'), x))
        # Definition of types of images to show.
        extensions = [".jpg", ".png", ".gif"]
        # Add photo names to the list
        for file_name in sorted_names:
            for extension in extensions:
                if file_name.endswith(extension):
                    self.photo_names.append(file_name)

    def __len__(self):
        return len(self.photo_names)

    def __getitem__(self, index):
        return self.photo_names[index]