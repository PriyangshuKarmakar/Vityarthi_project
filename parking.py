from records import add_parking_record,get_parking_records
def Add_Record():
    freespace = input("Is there any freespace or not (yes/no): ")
    if freespace.lower() == "yes":
      print("\n========== ADD PARKING DETAILS ==========")
      try:
          pid = int(input("Enter the parking number: "))
      except ValueError:
          print("Parking number must be a number.")
          return
      pname = input("Enter the Parking Name: ")
      level = input("Enter level of parking: ")
      vehicleno = input("Enter the Vehicle Number: ")
      try:
         nod = int(input("Enter total number of days for parking: "))
      except ValueError:
         print("Number of days must be a number.")
         return
      if nod <= 0:
          print("Number of days must be greater than zero.")
          return
      payment = 20 * nod
      record = {"pid": pid,
                "pnm": pname,
                "level": level,
                "freespace": freespace,
                "vehicleno": vehicleno,
                "nod": nod,
                "payment": payment}
      add_parking_record(record)
      print("\nParking record added successfully.")
      print("Total Payment :", payment)
    else:
        print("There is no freespace available.")
def Rec_View():
    print("\n========== VIEW PARKING DETAILS ==========")
    print("Select the search criteria:")
    print("1. Parking ID")
    print("2. Parking Name")
    print("3. Level Number")
    try:
        ch = int(input("Enter the choice: "))
    except ValueError:
        print("Invalid choice.")
        return
    records = get_parking_records()
    results = []
    if ch == 1:
        try:
            s = int(input("Enter Parking ID: "))
        except ValueError:
            print("Parking ID must be a number.")
            return
        for record in records:
            if record["pid"] == s:
                results.append(record)
    elif ch == 2:
        s = input("Enter Parking Name: ")
        for record in records:
            if record["pnm"].lower() == s.lower():
                results.append(record)
    elif ch == 3:
        s = input("Enter Level of Parking: ")
        for record in records:
            if record["level"].lower() == s.lower():
                results.append(record)
    else:
        print("Invalid search option.")
        return
    if len(results) == 0:
        print("\nNo parking record found.")
    else:
        for record in results:
            print("\n------------------------------")
            print("Parking Id :", record["pid"])
            print("Parking Name :", record["pnm"])
            print("Level :", record["level"])
            print("Freespace (Y/N) :", record["freespace"])
            print("Vehicle Number :", record["vehicleno"])
            print("Number of days for parking :", record["nod"])
            print("Payment :", record["payment"])
            print("------------------------------")
    print("\nTask completed.")