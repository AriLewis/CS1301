'''
Bulk Orders
Aryona Lewis
Description
'''
# Part 1: Defining the function

def compute_item_total(item):
    total = item['price'] * item['quantity']
    if item['quantity'] >= 10:
        total = total - total * .1
    return round(total, 2)

items = []
name = input("Enter item name (or 'done' \ 'd' to finish)")

while name != 'done' and name != 'd':
    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity ordered: "))

    item = {'name': name, 'price': price, 'quantity': quantity}
    items.append(item)

    name = input("Enter item name (or 'done' \ 'd' to finish)")

grand_total = 0
print("----- Order Summary -----")
for item in items:
    if item['quantity'] >= 10:
        status = "Discount"
    else: 
        status = "No discount"
    total = compute_item_total(item)
    print(f"{item['name']}  {item['quantity']} units {status} ${total:.2f}")
    grand_total += total

print(f"Order Total: $ {grand_total:.2f}")