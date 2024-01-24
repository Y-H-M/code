from PIL import Image
from rgbprint import rgbprint

im = Image.open(r"abc.jpg")

rgbprint("■", color=im.getpixel((0,0)))

print(im.size