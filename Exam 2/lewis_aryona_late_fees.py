'''
Program: Late fees
Author: Aryona Lewis
Description: Calculate late fees for overdue library books at $0.25 per overdue day.
'''

# Defining the function compute_late_fee() for overdue books and fee.

def compute_late_fee(book):
    if book['days_out'] > book['max_days']:
        overdue = book['days_out'] - book['max_days']
        fee = overdue * 0.25
    else:
        fee = 0.00
    return round(fee, 2)

# Main program: Setting up the while loop to assign the title of the book, days out, and max days to dictionary

books = []

title = input("Enter book title (or 'done'/'d' to finish): ")
while title != 'done' and title != 'd':
    days_out = int(input("Enter days checked out: "))
    max_days = int(input("Enter max borrowing days: "))

    book = {'title': title, 'days_out': days_out, 'max_days': max_days}
    books.append(book)

    title = input("Enter book title (or 'done'/'d' to finish): ")

# Creating the total
print("-------- Late Fee Summary --------")

grand_total = 0

for book in books:
    fee = compute_late_fee(book)
    if book['days_out'] > book['max_days']:
        overdue = book['days_out'] - book['max_days']
        status = f"{overdue} days overdue"
    else:
        status = "On time"
    print(f"{book['title']}   {status}   ${fee:.2f}")
    grand_total += fee

print("----------------------------------")
print(f"Total Fees Collected: ${grand_total:.2f}")
