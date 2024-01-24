from PIL import Image

im = Image.open(r"abc.jpg")

print(im.getpixel((0,0))