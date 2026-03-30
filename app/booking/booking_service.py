from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode
from datetime import datetime
from app.division.validation import Validation



class Booking_service:
    def __init__(self):
        self.file = Read_mode()
        self.writefile = Write_mode()
        self.tables = {}
        
    def table_booking(self):
        try:
            data = self.file.read_file("app/database/table.json")
            bookings = self.file.read_file("app/database/booking.json")

            customer_name = input("Enter customer name: ").title()
            obj1=Validation()
            obj1.username_validation(customer_name)
        
            people = int(input("Enter number of people: "))
            obj1=Validation()
            obj1.people_validation(people)
            
            table_no = int(input("Enter table number to book: "))
            obj1=Validation()
            obj1.table_no_validation(table_no)
            
            mobile_no = int(input("Please enter mobile number :"))
            obj1=Validation()
            obj1.mobile_no_validation(mobile_no)
            date = input("Enter booking date (DD-MM-YYYY): ")
            datetime.strptime(date, "%d-%m-%Y")
            
            start_time = input("Enter booking starting time (HH:MM): ")
            datetime.strptime(start_time, "%H:%M")
            
            end_time = input("Enter booking ending time (HH:MM): ")
            datetime.strptime(end_time, "%H:%M")
            

            found = False

            for table in data:
                if table["table_id"] == table_no:
                    found = True

                
                    if table["capacity"] < people:
                        print("Table capacity not enough ")
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
                    print("customer name:", customer_name)
                    print("booking time:", f"{date} {start_time} : {end_time}")
                    return

            if not found:
                print("Table not found ")

        except Exception as e:
            print("Error:", e)
            
    