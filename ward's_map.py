wards = {
    "Cardiology": ["Alice", "Bob", "Carol"],
    "Neurology": ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Mark"],
    "Oncology": ["Ivy", "Bob"]
}

def find(dept):
    looker = input("Find person")

    for scan, staff in dept:
        if scan in staff:
            break
        else: 
            if looker in dept:
                staff[scan] = {
                    dept
                }
    for scan in dept.items():
        print(scan)

find(wards)