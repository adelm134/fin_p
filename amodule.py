from PIL import Image, ImageFilter, ImageDraw, ImageFont
import os
from tkinter import filedialog
from tkinter import *

root = Tk()
root.title('Batch Image App')
root.iconbitmap('app//alatoo.ico')
root.geometry('300x300')

def Openfolder():
    root = Tk()
    root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",
                                                filetypes = (("jpeg files","*.jpg"), ("all files","*.*")))
    print (root.filename)
        
def batch():
    for pic in os.listdir('images'):
        if pic.endswith('.jpg' or '.png' or '.img' or '.jpeg'):
            img = Image.open(pic)
            fn, flext = os.path.splitext(pic)

            new = img.convert('L')
            new1 = new.filter(ImageFilter.DETAIL)
            new2 = new1.resize((1080, 1080))
            width, height = new2.size

            draw = ImageDraw.Draw(new2)
            text = "hii :>"
            title = "BLACK"
            font = ImageFont.truetype("app/font.ttf", 80)
            textwidth, textheight = draw.textsize(text, font)

            margin = 10
            x = width - textwidth - margin
            y = height - textheight - margin

            draw.text((x, y), text, title, font=font)

            new2.save('pic/{}{}'.format(fn, flext))