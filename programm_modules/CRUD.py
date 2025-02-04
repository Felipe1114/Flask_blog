import json
class Crud:
  def __init__(self, file_path:str):
    self.file_path = file_path


  def get_posts(self) -> list:
    """returns blog posts; if FileNotFoundError: a new file with empty list is created"""
    try:
      with open(self.file_path, 'r') as json_obj:
        data = json.load(json_obj)

      return data

    except FileNotFoundError:
      with open(self.file_path, 'w') as json_obj:
        json.dump([], json_obj, indent=4)

      return []

