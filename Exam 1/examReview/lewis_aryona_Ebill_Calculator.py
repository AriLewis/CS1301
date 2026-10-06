'''
EBill Calculator
Aryona Lewis
Calculating the total cost of power depending on the type of customer they are and how many units they have.
'''
customer = str(input("What type of unit do you have? "))
units = int(input("How many units do you have? "))

rates = {
            "residential": 0.12,
            "commercial": 0.18,
            "industrial": 0.25
}


if customer in rates:
    if rates["residential"]:
        base_cost = rates["residential"]*units
        if units < 100:
            usage = "Low Usage:"
            total_cost = base_cost
        elif units == 100 or units < 500:
            usage = "Moderate Usage"
            total_cost = base_cost*(1+.08)
        elif units > 500:
            usage = "High Usage"
            total_cost = base_cost*(1+.15)
    elif rates["commercial"]:
        base_cost = rates["commercial"]*units
        if units < 100:
            usage = "Low Usage:"
            total_cost = base_cost
        elif units == 100 or units < 500:
            usage = "Moderate Usage"
            total_cost = base_cost*(1+.08)
        elif units > 500:
            usage = "High Usage"
            total_cost = base_cost*(1+.15)
    elif rates["industrial"]:
        base_cost = rates["industrial"]*units
        if units < 100:
            usage = "Low Usage:"
            total_cost = base_cost
        elif units == 100 or units < 500:
            usage = "Moderate Usage"
            total_cost = base_cost*(1+.08)
        elif units > 500:
            usage = "High Usage"
            total_cost = base_cost*(1+.15)
    print(f"{customer} {units} khw {usage} ${total_cost}")
else:
    print("Error")