from PIL import Image
from rgbprint import rgbprint

im = Image.open(r"abc.jpg")

print("■", color=im.getpixel(0,0))
