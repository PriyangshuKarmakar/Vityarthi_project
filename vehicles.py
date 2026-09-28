from records import ( add_vehicle_record,
    get_vehicle_records,
    delete_vehicle_record )
def Vehicle_Detail():
    print("\n========== ADD VEHICLE DETAILS ==========")
    vid = input("Enter Vehicle No: ")
    vnm = input("Enter Vehicle Name/Model Name: ")
    dateofpur = input("Enter Date-Month-Year of purchase: ")
    record = { "pid": vid,
        "vehiclename": vnm,
        "dateofpur": dateofpur }
    add_vehicle_record(record)
    print("\nVehicle details added successfully.")
def remove():
    print("\n========== REMOVE VEHICLE RECORD ==========")
    vid = input("Enter the vehicle number of the vehicle to be deleted: ")
    found = delete_vehicle_record(vid)
    if found:
        print("Vehicle record removed successfully.")
    else:
        print("Vehicle record not found.")
def Vehicle_View():
    print("\n========== VIEW VEHICLE DETAILS ==========")
    vid = input("Enter the vehicle number of the vehicle whose details are to be viewed: ")
    records = get_vehicle_records()
    results = []
    for record in records:
        if record["pid"] == vid:
            results.append(record)
    print("\nThe following are the details you wanted:")
    if len(results) == 0:
        print("No vehicle record found.")
    else:
        for record in results:
            print("\n------------------------------")
            print("Vehicle Number :", record["pid"])
            print("Vehicle Name :", record["vehiclename"])
            print("Date of Purchase :", record["dateofpur"])
            print("------------------------------")
    print("\nTask completed.")