import json
import os
from typing import Dict, List

current_dir = os.path.dirname(__file__)
data_path = 'data.json'
abs_path = os.path.join(current_dir, data_path)


def read_data() -> List[Dict]:
    """ Get all data from data.json file.

  Reads all data from the json file and returns a list
  containing all data.
  """
    with open(abs_path, 'r') as file:
        json_text = file.read()
    data = json.loads(json_text)
    return data
