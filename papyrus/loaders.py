from zipfile import ZipFile
import os


class CBZLoader:
    def __init__(self, file):
        self.file = file
        self.zip_basename = os.path.splitext(os.path.basename(file))[0]

    def get_pages_list(self):
        with ZipFile(self.file) as archive:
            pages_list = [
                item.split('/')[1]
                for item in archive.namelist()
                if item != f"{self.zip_basename}/"
            ]
        return pages_list
