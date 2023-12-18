import os
from PIL import Image

def resize_images():
    for filename in os.listdir('./'):
        if filename.endswith('.jpg') or filename.endswith('.jpeg'):
            img = Image.open(filename)
            wpercent = (150/float(img.size[0]))
            hsize = int((float(img.size[1])*float(wpercent)))
            img = img.resize((150,hsize), Image.ANTIALIAS)
            img.save(filename)

resize_images()