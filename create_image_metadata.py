from layer_manager import LayerManager
import util
import random
import json


TOTAL_IMAGES = 20
all_images = []
lm = LayerManager()


def create_new_image():
  new_image = {}
  for layer_type in lm.layer_types:
    new_image[layer_type] = random.choices(lm.layer_ids[layer_type], lm.layer_weights[layer_type])[0]

  # infinite loop if not given enough layers to create a new unique image
  if new_image in all_images:
    return create_new_image() 
  else:
    return new_image


def create_image_collection():
  for i in range(TOTAL_IMAGES):
    unique_image = create_new_image()
    unique_image['tokenId'] = i + 1
    all_images.append(unique_image)


def create_json_metadata():
  util.create_dirs_for_path('./metadata/')
  with open('./metadata/image-traits.json', 'w+') as outfile:
      json.dump(all_images, outfile, indent=2)


if __name__ == "__main__":
  create_image_collection()
  create_json_metadata()