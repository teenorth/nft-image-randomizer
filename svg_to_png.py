import os
from cairosvg import svg2png
import util

file_list = list()
for root, dirs, files in os.walk("./svg_files"):
  for file in files:
    temp = {
      "path": root,
      "name": file
    }
    file_list.append(temp)


for file in file_list:
  dir_name = file["path"].split('/')[2]
  png_dir = f'./png_files/{dir_name}/'
  util.create_dirs_for_path(png_dir)
  file_path = f'{file["path"]}/{file["name"]}'
  file_name = file["name"].split('.')[0]
  write_path = f'./png_files/{dir_name}/{file_name}.png'

  svg2png(url=file_path, write_to=write_path)
  print(f'{file_path} to {write_path}')

print('Converted svgs to pngs!')