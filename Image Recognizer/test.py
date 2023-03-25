import os, random
from PIL import Image

img_name = random.choice(os.listdir("D:\Image Recognizer\processed data")) #change dir name to whatever
img = Image.open(f'D:/Image Recognizer/processed data/{img_name}').convert('RGB')
img.show()
