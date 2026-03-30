from app.file_handler.read_mode import Read_mode


class Billing_service:
    def __init__(self):
        self.file = Read_mode()
    
    def generate_bill(self):
        
        try:
            table_no = input("Enter Table Number for Bill: ")

            data = self.file.read_file("app/database/orders.json")

                
            if table_no not in data:
                print("No order found for this table ")
                return

            order = data[table_no]
            print("============================================================")
            print(" **********  VELVET VALLEY RESTAURANT  *********")
            print("            ========== BILL ===========")
            print("============================================================")
            print("Table No:", table_no)
            print("Customer:", order["customer_name"])
            
            total = 0
            for item in order["items"]:
                print("         ITEM :  ",  item["item"]) 
                print("         QUANTITY :" ,   item["quantity"])
                print("         PRICE :" ,  item["price"])
                total += int(item["quantity"]) * item["price"]

            print("     Total:",     total)
            print("============================================================")
            print("                  Thank You ! Visit Again                     ")
            print("============================================================")

        except Exception as e:
            print("Error:",e)