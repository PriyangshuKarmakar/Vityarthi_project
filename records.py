parking_records=[]
vehicle_records=[]
def add_parking_record(record):
    parking_records.append(record)
def get_parking_records():
    return parking_records
def add_vehicle_record(record):
    vehicle_records.append(record)
def get_vehicle_records():
    return vehicle_records
def delete_vehicle_record(vehicle_number):
    found = False
    for record in vehicle_records[:]:
        if record["pid"] == vehicle_number:
            vehicle_records.remove(record)
            found = True
    return found