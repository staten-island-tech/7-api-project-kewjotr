wards = {
    "Cardiology": ["Alice", "Bob", "Carol"],
    "Neurology": ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Mark"],
    "Oncology": ["Ivy", "Bob"]
}


def find(dept):
    staff = {}
    department = []
    docfinder = input("")
    for keys, values in dept.items():
        if docfinder in staff:
            department.append(keys)
        elif docfinder == values:
            staff = {docfinder}
            department.append(keys)
    print(docfinder)
    print(department)

find(wards)