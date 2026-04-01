from datetime import datetime

def write_log(message):
    with open("app/logs/log.txt","a") as file:
        time= datetime.now()
        file.write( str(time) + "-" + message + "\n" )
        