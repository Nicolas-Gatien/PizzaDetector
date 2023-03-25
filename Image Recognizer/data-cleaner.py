import os
import json
from PIL import Image

f = open('data.json')
data = json.load(f)

global_pizza_number = data['pizzas']
global_other_number = data['others']

pizza_path = 'D:/Image Recognizer/raw data/pizza'
not_pizza_path = 'D:/Image Recognizer/raw data/notpizza'

for path, subdirs, files in os.walk(pizza_path):
   for name in files:
      img = Image.open(os.path.join(path, name))
      print(os.path.join(path, name))
      global_pizza_number += 1
      width, height = img.size   # Get dimensions

      final_size = 0
      if (width > height):
         final_size = height
      else:
         final_size = width
              

      left = (width - final_size)/2
      top = (height - final_size)/2
      right = (width + final_size)/2
      bottom = (height + final_size)/2

      # Crop the center of the image
      img = img.crop((left, top, right, bottom))
      img = img.resize((28, 28))
      img.save(f"D:/Image Recognizer/processed data/pizza{global_pizza_number}.png")
      os.remove(os.path.join(path, name))

for path, subdirs, files in os.walk(not_pizza_path):
   for name in files:
      img = Image.open(os.path.join(path, name))
      print(os.path.join(path, name))
      global_other_number += 1
      width, height = img.size   # Get dimensions

      final_size = 0
      if (width > height):
         final_size = height
      else:
         final_size = width
              

      left = (width - final_size)/2
      top = (height - final_size)/2
      right = (width + final_size)/2
      bottom = (height + final_size)/2

      # Crop the center of the image
      img = img.crop((left, top, right, bottom))
      img = img.resize((28, 28))
      img.save(f"D:/Image Recognizer/processed data/not{global_other_number}.png")  
      os.remove(os.path.join(path, name))

with open('data.json', 'w') as f:
   numbers = {
      "pizzas": global_pizza_number,
      "others": global_other_number
   }
   json.dump(numbers, f)


