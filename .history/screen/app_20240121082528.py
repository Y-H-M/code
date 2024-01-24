from PIL import Image
from rgbprint import rgbprint

im = Image.open(r"abc.jpg")

rgbprint("■", color=im.getpixel((0,0)))

for i in range(im.size[0]):
    for j in range(im.size[1]):
        rgbprint("■", color=im.getpixel((i,j)), end="")