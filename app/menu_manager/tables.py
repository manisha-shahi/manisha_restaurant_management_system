import json

def table_data():
    data = []

    for i in range(1, 56):   
        table = {
            "table_id": i,
            "capacity": 4 ,  
            "status": "available"
        }
        data.append(table)

    with open("app/database/table.json", "w") as file:
        json.dump(data, file, indent=4)

    return data

table_data()