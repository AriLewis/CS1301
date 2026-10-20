count = int(input("Please enter the number of floating-point values: "))

values = []
for i in range(count):
    value = float(input("Please enter a floating-point value: "))
    values.append(value)

largest = max(values)

print()
print("Normalized Floating-Point Values:")
for value in values:
    print(f"{value / largest:.2f}")