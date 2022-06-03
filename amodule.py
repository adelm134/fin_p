from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title('Batch Image App')
root.iconbitmap('app//alatoo.ico')

for k in os.listdir('.'):
    if k.endswith('.jpg') or k.endswith('.png'):
        i = Image.open(k)
        fn, flext = os.path.splitext(k)

        #watermark
        w = Image.open(k)
        width, height = w.size
        draw = ImageDraw.Draw(w)
        text = "HII :>"
        title = "black"
        font = ImageFont.truetype("app/font.ttf", 90)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)
        
        ifl = i.filter(ImageFilter.DETAIL)
        # Resize Image
        ir = i.resize((1080, 1080))
        # Convert Image to Black and White
        ibw = i.convert('L')

        res = i.convert('L')
        res1 = res.filter(ImageFilter.DETAIL)
        res2 = res1.resize((1080, 1080))
        width, height = res2.size

        draw = ImageDraw.Draw(res2)
        text = "HII :>"
        title = "black"
        font = ImageFont.truetype("app/font.ttf", 90)
        textwidth, textheight = draw.textsize(text, font)

        margin = 10
        x = width - textwidth - margin
        y = height - textheight - margin

        draw.text((x, y), text, title, font=font)
        
        ir.save('pics/{}{}'.format(fn, flext))
        ifl.save('pics/{}{}'.format(fn, flext))
        ibw.save('pics/{}{}'.format(fn, flext))
        w.save('pics/{}{}'.format(fn, flext))
        res2.save('pics/{}{}'.format(fn, flext))
