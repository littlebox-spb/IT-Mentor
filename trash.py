def update_order(new_item, current_order=[]):
    current_order.append(new_item)
    return current_order


order1 = update_order({"item": "burger", "cost": 103.5})

order2 = update_order({"item": "soda", "cost": 51.5})

print(order2)
