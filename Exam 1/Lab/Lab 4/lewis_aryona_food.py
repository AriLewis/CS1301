menu = {"hot_dog": 1.50,
                        "Slice": 1.99,
                        "Whole": 9.95,
                        "Soft_Drink": 0.59,
                        }

hot_dog = int(input("Please enter the number of Hot Dogs: "))
slices = int(input("Please enter the number of Pizza Slices: "))
whole = int(input("Please enter the number of Whole Pizzas: "))
soft_drink = int(input("Please insert the number of Soft Drinks: "))

total = (hot_dog * menu["hot_dog"] + 
        slices * menu["Slice"] +
        whole * menu["Whole"]+
        soft_drink * menu["Soft_Drink"]
    )

print(f"The total cost of the order is ${total:.2f}")
