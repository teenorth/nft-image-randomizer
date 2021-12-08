import json
import os

LAYER_META_URL='./layer_manager/layer-metadata.json'
weights = {
  'common': 50,
  'uncommon': 35,
  'exotic': 20,
  'legendary': 10,
  'mythic': 5,
}


class LayerManager():
  layer_data = {}
  layer_weights = {}
  layer_ids = {}
  layer_types = []


  def __init__(self):
    self.open_layer_json()
    self.process_layers()


  def open_layer_json(self):
    with open(LAYER_META_URL) as file:
      data = json.load(file)
      file.close()
    self.layer_data = data


  def process_layers(self):
    for layer_type, layers in self.layer_data.items():
      self.layer_types.append(layer_type)
      self.layer_ids[layer_type] = []
      self.layer_weights[layer_type] = []
      for layer_id, layer in layers.items():
        if layer['rarity']:
          self.layer_data[layer_type][layer_id]['rarity'] = weights[layer['rarity']]
        else:
          self.layer_data[layer_type][layer_id]['rarity'] = weights['common']
        self.layer_ids[layer_type].append(layer_id)
        self.layer_weights[layer_type].append(layer['rarity'])
