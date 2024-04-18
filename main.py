import pytesseract
from PIL import Image, ImageOps 
import os 
import cv2 
import numpy as np


input_dir = 'images'

output_dir = 'output'


""" Borders """
border_width = 5
border_color = (0, 0, 0)

for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        try: 
            image = Image.open(os.path.join(input_dir, filename))

            upscale_factor = 2
            width, height = image.size
            """ upscale image """
            image = image.resize((width * upscale_factor, height * upscale_factor))
            """ add border """
            image = ImageOps.expand(image, border=border_width, fill=border_color)
            """ convert to BGR """
            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            """ Additional configs: psm (see page segmentation methods); """
            recognized_text = pytesseract.image_to_string(image, lang='heron_language', config='--psm 6')

            output_filename = os.path.splitext(filename)[0] + '.txt'
            with open(os.path.join(output_dir, output_filename), 'w') as output_file:
                output_file.write(recognized_text)

            print(f'Recognized text for {filename}: {recognized_text}')

        except Exception as e:
            print(f'Error processing {filename}: {str(e)}')


print ('Done! Finished OCR.')