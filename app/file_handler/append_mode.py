import json

class Append_mode:
                
    def append_file(self, path,order):
        try:
            with open(path, "a") as file:
                data = json.dump(order,file)
                return data
        except Exception as e:
            print(e)
            return []
