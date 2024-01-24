from PIL import Image
from rgbprint import rgbprint
from colorama import Fore, Style

im = Image.open(r"abc.jpg")

rgbprint("■", color=im.getpixel((0,0)))

for j in range(im.size[1]):
    for i in range(im.size[0]):
        rgbprint("■", color=im.getpixel((i,j)), end="")
    print()