import json

class Write_mode:

    def write_file(self, path, data):
        try:
            with open(path, "w") as file:
                json.dump(data, file, indent=4)
        except Exception as e:
            print(e)
           
