from PIL import Image
import glob, os

size = 28, 128

for infile in glob.glob("*.jpg"):
 file, ext = os.path.splitext(infile)
image = Image.open(infile)
image.thumbnail(size, Image.ANTIALIAS)
image.save(file + ".thumbnail", "JPEG")
print(image)