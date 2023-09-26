import glob
import os
import shutil

from PIL import Image, ImageEnhance, ImageOps


class Digitizer:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.img = Image.open(filepath)

    def save(self, dest_filepath):
        self.img.save(dest_filepath)

    def make_upside_down(self):
        self.img = self.img.rotate(180)

    def make_thumbnail_size(self, size=(128, 128)):
        self.img.thumbnail(size)

    def make_grayscale(self):
        self.img = ImageOps.grayscale(self.img)

    def adjust_contrast(self, amount=1.5):
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(amount)


inputs = glob.glob("inputs/*")
os.makedirs("outputs", exist_ok=True)

for filepath in inputs:
    output_path = filepath.replace("inputs", "outputs")
    image = Digitizer(filepath)
    # image.make_upside_down()
    # image.make_thumbnail_size()
    image.adjust_contrast(3.0)
    image.make_grayscale()
    image.save(output_path)
