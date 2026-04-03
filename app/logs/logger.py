from datetime import datetime

def write_log(level,message):
    with open("app/logs/log.txt","a") as file:
        time= datetime.now()
        file.write(f"{time} - {level} - {message}\n")
        