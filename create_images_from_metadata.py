from PIL import Image
import util
import json


IMAGE_METADAT_PATH="./metadata/image-traits.json"
all_images = []


if __name__ == "__main__":
  with open(IMAGE_METADAT_PATH) as file:
    all_images = json.load(file)
    file.close()

  for image in all_images:
    composed = None
    for layer_type, layer in image.items():
      if layer_type == 'tokenId': continue
      layer_path = f'./png_files/{layer_type}/{layer}.png'
      im = Image.open(layer_path).convert('RGBA')
      if composed:
        composed = Image.alpha_composite(composed, im)
      else:
        composed = im

    rgb_im = composed.convert('RGBA')
    file_name = str(image["tokenId"]) + ".png"
    file_path = "./images/"
    util.create_dirs_for_path(file_path)
    rgb_im.save(file_path + file_name)
    print('Created image: ', file_name)
