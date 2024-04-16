import pytesseract
from PIL import Image
import os 
import cv2 
import numpy as np


input_dir = 'images'

output_dir = 'output'


for filename in os.listdir(input_dir):
    if filename.endswith('.jpg') or filename.endswith('.png'):
        try: 
            image = Image.open(os.path.join(input_dir, filename))

            upscale_factor = 2
            width, height = image.size
            image = image.resize((width * upscale_factor, height * upscale_factor))

            image = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

            recognized_text = pytesseract.image_to_string(image, lang='heron_language')

            output_filename = os.path.splitext(filename)[0] + '.txt'
            with open(os.path.join(output_dir, output_filename), 'w') as output_file:
                output_file.write(recognized_text)

            print(f'Recognized text for {filename}: {recognized_text}')

        except Exception as e:
            print(f'Error processing {filename}: {str(e)}')


print ('Done! Finished OCR.')