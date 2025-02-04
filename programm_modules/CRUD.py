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


  def save_posts(self, new_data):
    """saves new data to json-file"""
    with open(self.file_path, 'w') as json_obj:
      json.dump(new_data, json_obj, indent=4)


  def get_id(self):
      """returns newest_blog_post_id"""
      blog_posts = self.get_posts()
      newest_id = blog_posts[-1]['id']

      return newest_id
