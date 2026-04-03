from app.division.json_manage import Json_Class
from datetime import datetime
from app.logs.logger import write_log

class Billing_service:
    
    def generate_bill(self):
        try:
            today = datetime.now().strftime("%d-%m-%Y %H:%M")
            table_no = input("\033[93m Enter Table Number for Bill: ").strip()
            json_obj2 = Json_Class()
            order_data = json_obj2.read_orders()

            if not order_data:
                print("\033[91m No orders available!")
                return

            if table_no not in order_data:
                print("\033[91m No order found for this table")
                print("\033[93m Please take order first")
                return

            order = order_data[table_no]

            if type(order) == dict:
                if "customer_name" in order:
                    customer_name = order["customer_name"]
                else:
                    customer_name = "Customer"

                if "items" in order:
                    items = order["items"]
                else:
                    items = []
            else:
             
                customer_name = "Customer"
                items = order

            print("\n" + "="*65)
            print(" \033[93m       VELVET VALLEY RESTAURANT ")
            print("                  BILL")
            print("="*65)
            print(f"Table No : {table_no}")
            print(f"Date     : {today}")
            print(f"Customer : {customer_name}")
            print("\n" + "-"*65)
            print(f"{'Item':<25}{'Qty':<10}{'Price':<10}{'Total':<10}")
            print("-"*65)

            total = 0
            for item in items:
                name = item["item"]
                qty = int(item["quantity"])
                price = int(item["price"])
                item_total = qty * price
                total += item_total

                print(f"{name:<25}{qty:<10}₹{price:<9}₹{item_total:<10}")

            print("-"*65)

            gst = total * 0.05
            final_total = total + gst

            print(f"{'Subtotal':<45} ₹{total}")
            print(f"{'GST (5%)':<45} ₹{gst:.2f}")
            print("="*65)
            print(f"{'Grand Total':<45} ₹{final_total:.2f}")
            print("="*65)
            print("\033[93m        Thank You! Visit Again ")
            print("="*65)

        except Exception as e:
            print("Error:", e)
            write_log("ERROR", f"Error during signup: {e}")