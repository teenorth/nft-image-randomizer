# NFT image randomizer

## How to use

If your using png files from the start create a folder structure like this:

```
png_files/
├─ background/
│  ├─ background-01.png
│  ├─ background-02.png
├─ base/
│  ├─ base-01.png
│  ├─ base-02.png
│  ├─ base-03.png
```

If your using svg files create a folder structure like png files:

```
svg_files/
├─ background/
│  ├─ background-01.svg
│  ├─ background-02.svg
├─ base/
│  ├─ base-01.svg
│  ├─ base-02.svg
│  ├─ base-03.svg
```

Then run svg_to_png.py and it will create the png_files structure for you.


## Using layer-metadata.json

Now that you have your images ready to go you have to create your json to go along with the files. This defines the structure of how your images will be stacked on top of each other. It also allows you to define the chance for each layer and a name to be used instead of the file name.

Rarity defines the chance of that layer getting used in the image. If no rarity is provided Common will be used.

Rarity types:
- Common - 50
- Uncommon - 35
- Exotic - 20
- Legendary - 10
- Mythic - 5


Writting the layer-metadata file:

```json
{
  "background": { 
    "background-01": { <-- this must match the file name without .png
      "rarity": "common",
    },
    "background-02": {
      "rarity": "exotic",
    }
  },
  "base": {
    "base-01": {
      "rarity": "legendary",
    },
    "base-02": {
      "rarity": "mythic",
    },
    "base-03": {
      "rarity": "uncommon",
    }
  },
  "next_layer": {
    ...
  }
}
```

This file should match your folder structure, this will be used to then go fetch the images from the folders so the names must match. It's also important to note that if I was to put base as the first json entry that would be the first layer to be picked. This examples will go background -> base -> next_layer.


## Creating the images

Once you have your layer-metadata created and the png files to go along with it. You can run:

Note: create_image_metadata.py has a variable called TOTAL_IMAGES this is how many will be created.

```bash
python3 create_image_metadata.py
```

I seperated the image creating function from this file to allow you to create unique images within the /metadata/image-traits.json file that was created.

This is an example image metadata:

```json
{
  "background": "background-03",
  "base": "base-01",
  "eyes": "eyes-06",
  "head": "head-19",
  "neck": "neck-59",
  "ear": "ear-14",
  "tokenId": 1
}
```

You can modify the above json with the png files that you like to create unique rare images.

Once your happy with your image traits. You can run:

```bash
python3 create_images_from_metadata.py
```

You should now see a folder called images with the results from image-traits.json.

## Cairo install

```bash
# install cairosvg
pip3 install cairosvg

# try import cairosvg
python3
>>> import cairosvg

# if you get an error download this file
wget https://downloads.sk1project.net/uc2/Ubuntu/python-uniconvertor-2.0rc5_ubuntu_20.04_amd64.deb

# install the file
sudo dpkg -i python-uniconvertor-2.0rc5_ubuntu_20.04_amd64.deb

# if that throws an error
sudo apt --fix-broken install
```

That should be cairo installed.

## Pillow install

```bash
pip3 install pillow
```
