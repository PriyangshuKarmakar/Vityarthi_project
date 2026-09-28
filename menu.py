from parking import Add_Record,Rec_View
from vehicles import Vehicle_Detail,remove,Vehicle_View
def Menu():
    while True:
        print("\n========== PARKING MANAGEMENT SYSTEM ==========")
        print("Enter 1 : To Add Parking Details")
        print("Enter 2 : To View Parking Details")
        print("Enter 3 : To Add Vehicle Details")
        print("Enter 4 : To Remove Vehicle Record")
        print("Enter 5 : To See the Details of Vehicle")
        print("Enter 6 : To Exit")
        try:
            input_dt = int(input("Please Select An Above Option: "))
        except ValueError:
            print("Please enter a valid number.")
            continue
        if input_dt == 1:
            Add_Record()
        elif input_dt == 2:
            Rec_View()
        elif input_dt == 3:
            Vehicle_Detail()
        elif input_dt == 4:
            remove()
        elif input_dt == 5:
            Vehicle_View()
        elif input_dt == 6:
            print("Thank you for using the Parking Management System.")
            break
        else:
            print("Invalid option entered.")
def runAgain():
    while True:
        if_run = input("If you want to run Again (yes/no): ").lower()
        if if_run == "yes":
            Menu()
            break
        elif if_run == "no":
            print("Thank you for using the Parking Management System.")
            break
        else:
            print("Invalid input.")