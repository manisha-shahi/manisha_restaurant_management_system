from app.file_handler.read_mode import Read_mode

class ReportManager:
    def __init__(self):
        self.file = Read_mode()

   
    def sales_report(self):
        try:
            data = self.file.read_file("app/database/orders.json")

            sales_per_day = {}

            for table_no, order in data.items():
                if type(order) == dict:
                    items = order["items"] if "items" in order else []
                    order_date = order["date"] if "date" in order else "Unknown"
                else:
                    items = order
                    order_date = "Unknown"

                day_total = 0
                for item in items:
                    qty = int(item["quantity"])
                    price = int(item["price"])
                    day_total += qty * price

                if order_date in sales_per_day:
                    sales_per_day[order_date] += day_total
                else:
                    sales_per_day[order_date] = day_total

            print("\n📊 SALES PER DAY")
            print("="*40)
            for date in sales_per_day:
                print(f"{date:<15}  Total Sales: ₹{sales_per_day[date]}")
            print("="*40)

            top_day = None
            max_sales = 0
            for date in sales_per_day:
                if sales_per_day[date] > max_sales:
                    max_sales = sales_per_day[date]
                    top_day = date
            if top_day:
                print(f"\033[92m Top Selling Day: {top_day}  Sales: ₹{max_sales}")
            print("="*40)

        except Exception as e:
            print("Error:", e)

   
    def booking_report(self):
        try:
            data = self.file.read_file("app/database/booking.json")

            booking_per_day = {}

            for booking in data:
                date = booking["date"] if "date" in booking else "Unknown"
                if date in booking_per_day:
                    booking_per_day[date] += 1
                else:
                    booking_per_day[date] = 1

            print("\n \033[92m BOOKINGS PER DAY")
            print("="*40)
            for date in booking_per_day:
                print(f"{date:<15}  Bookings: {booking_per_day[date]}")
            print("="*40)

          
            top_day = None
            max_booking = 0
            for date in booking_per_day:
                if booking_per_day[date] > max_booking:
                    max_booking = booking_per_day[date]
                    top_day = date
            if top_day:
                print(f"\033[92m Day with Maximum Booking: {top_day}  Bookings: {max_booking}")
            print("="*40)

        except Exception as e:
            print("Error:", e)

   
    def menu_report(self):
        try:
            data = self.file.read_file("app/database/orders.json")

            dish_count = {}

            for table_no, order in data.items():
                if type(order) == dict:
                    items = order["items"] if "items" in order else []
                else:
                    items = order

                for item in items:
                    name = item["item"]
                    qty = int(item["quantity"])
                    if name in dish_count:
                        dish_count[name] += qty
                    else:
                        dish_count[name] = qty

            print("\n\033[92m TOP SELLING DISHES")
            print("="*40)
            for dish in dish_count:
                print(f"{dish:<25} Quantity Sold: {dish_count[dish]}")
            print("="*40)

            top_dish = None
            max_qty = 0
            for dish in dish_count:
                if dish_count[dish] > max_qty:
                    max_qty = dish_count[dish]
                    top_dish = dish
            if top_dish:
                print(f"\n\033[92m Most Popular Dish: {top_dish}  Quantity Sold: {max_qty}")
            print("="*40)

        except Exception as e:
            print("Error:", e)