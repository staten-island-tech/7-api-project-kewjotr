wards = {
    "Cardiology": ["Alice", "Bob", "Carol"],
    "Neurology": ["Diana", "Eve"],
    "Orthopedics": ["Frank", "Grace", "Mark"],
    "Oncology": ["Ivy", "Bob"]
}

staff = {}

def find(dept):
    for dept, docs in wards.items():
        print(dept, docs)
        for doc in docs:
            print(doc)

find(wards)