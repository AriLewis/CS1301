'''
Lab Exam 2: Version D
Program: bulk_order.py
Part 1: compute_item_total()
Part 2: Main Program
'''

# Part 1: compute_item_total()
# { 'name': 'Notebook', 'price': 2.50, 'quantity': 12}

def compute_item_total(item):
    total = item['price'] * item['quantity']
    if item['quantity'] >= 10:
        total = total - total * 0.1
    return round(total, 2)

# Part 2: Main Program


items = []

name = input("Please enter item name (or 'done'/'d' to finish):")
while name != 'done' and name != 'd':
    price = float(input("Please enter item price:"))
    quantity = int(input("Please enter item quantity:"))

    item = { 'name': name, 'price': price, 'quantity': quantity}
    items.append(item)
    name = input("Please enter item name (or 'done'/'d' to finish):")

print("----------order Summary -----------")

grand_total = 0
for item in items:
    total = compute_item_total(item)
    if item['quantity'] >= 10:
        status = "Discount"
    else: 
        status = 'No Discount'
    print(f"{item['name']} {item['quantity']} units {status} ${total:.2f}")
    grand_total += total
print('-----------------------')
print(f"The total cost of the items is ${grand_total:.2f}")