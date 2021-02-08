import sys
import os
from PIL import Image

#* Grab first and second argument.
image_folder = sys.argv[1]   # PokeDex\\ 
output_folder = sys.argv[2]  # new\\
print(image_folder, output_folder)

#* Check if new folder exist, if not then create it.
# print(os.path.exists(output_folder))
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#* Loop through PokeDex.
for filename in os.listdir(image_folder):
    img = Image.open(f'{image_folder}{filename}')
    clean_extension = os.path.splitext(filename)[0]   # Removing existing extension i.e. JPG.
    img.save(f'{output_folder}{clean_extension}.png', 'png')   #* Convert images to PNG & save.
    print('Converted!')