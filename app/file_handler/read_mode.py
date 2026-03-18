import json

class Read_mode:

    def read_file(self, path):
        try:
            with open(path, "r") as file:
                data = json.load(file)
                return data
        except Exception as e:
            print(e)
            return []

   