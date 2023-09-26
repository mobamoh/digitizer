import glob
import os
import shutil

from digitizer import Digitizer

if __name__ == "__main__":
    inputs = glob.glob("inputs/*")
    os.makedirs("outputs", exist_ok=True)

    for filepath in inputs:
        output_path = filepath.replace("inputs", "outputs")
        image = Digitizer(filepath)
        # image.make_upside_down()
        # image.make_thumbnail_size()
        # image.adjust_contrast(3.0)
        # image.make_grayscale()
        # image.make_square()
        image.convert_to_ascii()
        image.add_watermark()
        image.save(output_path)
