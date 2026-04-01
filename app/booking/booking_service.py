from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from datetime import datetime
from app.division.validation import Validation
from app.logs.logger import write_log



class Booking_service:
    def __init__(self):
        self.file = Read_mode()
        self.writefile = Write_mode()
        self.tables = {}
        
    def table_booking(self):
        try:
            data = self.file.read_file("app/database/table.json")
            bookings = self.file.read_file("app/database/booking.json")

            customer_name = input("\033[93mEnter customer name: ").title()
            obj1=Validation()
            if not obj1.username_validation(customer_name):
                print("\033[91minvalid customer name")
                return
            
            people = int(input("\033[93m Enter number of people: "))
            
            table_no = int(input("\033[93m Enter table number to book: "))
               
            mobile_no = input("\033[93m Please enter mobile number :").strip()
            obj1=Validation()
            if not obj1.mobile_no_validation(mobile_no):
                print("\033[91m invalid mobile number")
                return
            
            date = input("\033[93m Enter booking date (DD-MM-YYYY): ")
            datetime.strptime(date, "%d-%m-%Y")
            
            start_time = input("\033[93m Enter booking starting time (HH:MM): ")
            datetime.strptime(start_time, "%H:%M")
            
            end_time = input("\033[93m Enter booking ending time (HH:MM): ")
            datetime.strptime(end_time, "%H:%M")
            

            found = False

            for table in data:
                if table["table_id"] == table_no:
                    found = True

                
                    if table["capacity"] < people:
                        print("\033[91m Table capacity not enough ")
                        return
                    
                    for details in bookings:
                        if details["table_id"] == table_no and details["date"] == date:
                            if start_time < details["end_time"] and end_time > details["start_time"]:
                                print(f"Table {table_no} already booked for {date} {start_time}-{end_time}")
                                return
                    
                    table["status"] = "booked"
                    table["customer_name"] = customer_name

                    new_booking = {
                        "table_id": table_no,
                        "customer_name": customer_name,
                        "mobile_no":mobile_no,
                        "date": date,
                        "start_time": start_time,
                        "end_time": end_time
                    }

                    bookings.append(new_booking)

                    self.writefile.write_file("app/database/table.json", data)
                    self.writefile.write_file("app/database/booking.json", bookings)

                    print(f"Table {table_no} booked successfully")
                    write_log("booked successfully :", customer_name)
                    print("customer name:", customer_name)
                    print("booking time:", f"{date} {start_time} : {end_time}")
                    return

            if not found:
                print("\033[91m Table not found ")

        except Exception as e:
            print("Error:", e)
            
    