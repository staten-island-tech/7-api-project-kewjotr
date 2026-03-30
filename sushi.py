sushi_orders = [
    {"name": "California Roll", "price": 8},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8},
    {"name": "Dragon Roll", "price": 12},
    {"name": "Spicy Tuna Roll", "price": 10},
    {"name": "Miso Soup", "price": 4},
    {"name": "Edamame", "price": 5},
    {"name": "Salmon Nigiri", "price": 6},
    {"name": "California Roll", "price": 8}
]

def receipt(orders):
    receipt = []
    for order in orders:
        if order['name'] in receipt:
            receipt[order['name'['quantity']]] += 1
        else:
            receipt[order['name']] = {
                "price": order['price'],
                "quantity": 1
            }
    print(receipt)
receipt(sushi_orders)
        