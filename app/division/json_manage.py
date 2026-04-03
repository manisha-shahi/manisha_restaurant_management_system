from app.file_handler.read_mode import Read_mode
from app.file_handler.write_mode import Write_mode

class Json_Class:
    
    def __init__(self):
        self.read_files = Read_mode()
        self.write_flies = Write_mode()
        
    def read_table(self):
        data = self.read_files.read_file("app/database/table.json")
        return data
    def write_table(self,data):
        self.write_flies.write_file("app/database/table.json", data)
        
    def read_user(self):
        listdata = self.read_files.read_file("app/database/user.json")
        return listdata
        
    def write_user(self,listdata):
        self.write_flies.write_file("app/database/user.json", listdata )
        
    def read_booking(self):
        bookings = self.read_files.read_file("app/database/booking.json")
        return bookings
        
    def write_booking(self,bookings):
        self.write_flies.write_file("app/database/booking.json",bookings )
        
    def read_item(self):
        item_data = self.read_files.read_file("app/database/item_data.json")
        return item_data
    
    def write_item(self,item_data):
        self.write_flies.write_file("app/database/item_data.json",item_data )
        
    def read_orders(self):
        order_data = self.read_files.read_file("app/database/orders.json")
        return order_data
        
    def write_orders(self,order_data):
        self.write_flies.write_file("app/database/orders.json", order_data)
    
    
    
    
    
    
    
    
    
   
        
    
    
   
    
    
    