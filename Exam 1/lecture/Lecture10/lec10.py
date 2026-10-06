'''Quiz 1 and exams next week. Only one coding on lab and it's branching related. One cheatsheet allowed on both sides.'''
#For Loops 
for i in ["Apple", "Banana", "Cherry"]:
    print("i")

students = ["Alice", "Bob", "Carol", "Emil"]
for i in students:
    print(f"Hello {i}") #give i a better variable name. 

for number in range(1, 11):
    print(number, end= " ")

for number in range(1, 21, 4):
    print(number, end= " ")

# Nested Loops

fruits = ["apple", "cherry", "bananas"]
colors = ["White", "black"]

for fruit in colors:
    for fruit in fruits:
        print(f"({colors}, {fruits})") #white apple white bannans... black apple black banana...colors

for i in range(1,3):
    for j in range(100, 103):
        print(f"({i}, {j})")

for i in range(1, 6):
    for j in range(i):
        print("*", end=" ") #loop iterated 5x
    print()

for num in range(1,100):
    if number == 5:
        print("Found 5! Stopping . . . ")
        break # ends the loop
    print(num)

names = ["Alice", "bob", "Charlie", "David", "Emma"]
search_name = "Charlie"

for name in names: 
    if name == search_name:
        print(f"Found {search_name}!")
        break
else: 
    print(f"{search_name} not found")

for num in range(1, 11):
    if num % 2 == 0:
        continue #skips current interation, then continues. 
    print(num)

for x in range(6):
    if x == 100:break
    print(x)
else:
    print("Finally Finished") #get everything, but doesnt excecute the break statement

# While loop

count = 0
while count < 5:
    print("Count is: ", count)
    count += 1 # if you block this out, you get an infinite loop
print("Done") 

n = 10
while n > 0:
    print(n)
    n -= 5

print("Blast off!") # prints only 10 and 5 for blast off. 

#difference between a for loop and a while loop: while when you dont know how many lopps to run. While for is for when you know how many you want to do. 

prices = [10.99, 5.50, 23.00, 8.75]
print(sum(prices))

prices = [10.99, 5.50, 23.00, 8.75]
total = 0
for price in prices:
    total += price
print(f"Total: ${total:.2f}")

# you have to define total outside of the for loop so it doesnt keep restarting over and over. 