from PIL import Image, ImageDraw, ImageEnhance, ImageFont, ImageOps


class Digitizer:
    def __init__(self, filepath) -> None:
        self.filepath = filepath
        self.img = Image.open(filepath).convert("RGBA")

    def save(self, dest_filepath):
        if self.filepath.endswith(".jpg"):
            self.img = self.img.convert("RGB")
        self.img.save(dest_filepath)

    def make_upside_down(self):
        self.img = self.img.rotate(180)

    def make_thumbnail_size(self, size=(128, 128)):
        self.img.thumbnail(size)

    def make_grayscale(self):
        self.img = ImageOps.grayscale(self.img)
        self.img = self.img.convert("RGBA")

    def adjust_contrast(self, amount=1.5):
        enhancer = ImageEnhance.Contrast(self.img)
        self.img = enhancer.enhance(amount)

    def make_square(self, size=200):
        (w, h) = self.img.size
        if w > h:
            x = (w - h) * 0.5
            y = 0
            box = (x, y, h + x, h + y)
        else:
            x = 0
            y = (h - w) * 0.5
            box = (x, y, x + w, y + w)

        self.img = self.img.resize((size, size), box=box)

    def add_watermark(self):
        fnt = ImageFont.truetype("ibm-plex-mono.ttf", 24)
        drawer = ImageDraw.Draw(self.img)
        drawer.text((32, 32), "Mo Bamoh", font=fnt, fill=(255, 215, 0))

    def convert_to_ascii(self):
        letters = [" ", ".", "!", "e", "b", "H", "a", "M", "d", "O"]
        fnt_size = 10
        (w, h) = self.img.size
        nw = int(w / fnt_size)
        nh = int(h / fnt_size)
        sample_size = (nw, nh)
        final_size = (nw * fnt_size, nh * fnt_size)

        self.make_grayscale()
        self.adjust_contrast(5.0)
        self.img = self.img.resize(sample_size)

        ascii_img = Image.new("RGBA", final_size, color="#1b1b1b")
        fnt = ImageFont.truetype("ibm-plex-mono.ttf", fnt_size)
        drawer = ImageDraw.Draw(ascii_img)

        for x in range(nw):
            for y in range(nh):
                (r, g, b, a) = self.img.getpixel((x, y))
                brightness = r / 256
                letter = letters[int(len(letters) * brightness)]
                position = (x * fnt_size, y * fnt_size)
                drawer.text(position, letter, font=fnt, fill=(255, 196, 137, 60))

        self.img = ascii_img
