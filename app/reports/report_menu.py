from app.reports.report import ReportManager
from app.logs.logger import write_log
class Reportmenu:
    def menu(self):
        while True:
            try:
                print(" ********* Report Menu ********* ")
                print("1.Menu Report")
                print("2.Booking Report")
                print("3.Sales Report")
                choice = input("\033[92mplease enter your choice :")
                if choice.isdigit():
                    choice=int(choice)
                    
                    if choice == 1:
                        ob = ReportManager()
                        ob.menu_report()
                        
                    elif choice == 2:
                        ob = ReportManager()
                        ob.booking_report()
                        
                    elif choice == 3:
                        ob = ReportManager()
                        ob.sales_report()
                    else:
                        print("\033[91m invalid choice ")
                        break
            except Exception as e:
                print("Error:",e) 
                write_log("Error during signup: ",e)
        
        
        
        