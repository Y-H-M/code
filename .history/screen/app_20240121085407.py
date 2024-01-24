from PIL import Image
from rgbprint import rgbprint
from colorama import Fore, Style

im = Image.open(r"abc.jpg")

rgbprint("■", color=im.getpixel((0,0)))

for j in range(im.size[1]):
    for i in range(im.size[0]):
        rgb = tuple(max(0, min(255, val)) for val in im.getpixel(i,j))
        color_code = f""
        rgbprint("■", color=im.getpixel((i,j)), end="")
    print()