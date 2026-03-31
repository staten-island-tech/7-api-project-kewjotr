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
    receipt = {}
    for sushi in orders:
        if sushi['name'] in receipt:
            receipt[sushi['name']]['quantity'] += 1
        else:
            receipt[sushi['name']] = {
                'price': sushi['price'],
                "quantity": 1
            }
    for sushi, value in receipt.items():
        price = value['price'] * value['quantity']
        print(sushi, value['quantity'], price)

receipt(sushi_orders)