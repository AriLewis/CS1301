'''Aryona Lewis, Intersate, gives number of interstate and information of that interstate'''

interstate = int(input("Please enter an interstate number: "))

if 1 <= interstate and interstate <= 99:
    if interstate % 2 != 0:
        direction = "north/south"
    else:
        direction = "east/west"
    print(f"I-{interstate} is primary, going {direction}.")
elif 100 <= interstate and interstate <= 999:
    primary= interstate % 100
    
    if primary == 0:
        print(f"{interstate} is not a valid interstate highway number.")
    else:
        if primary % 2 != 0:
            direction = "north/south"
        else:
            direction = "east/west"
        print(f"I-{interstate} is auxiliary, serving I-{primary}, going {direction}.")
else:
    print(f"{interstate} is not a valid interstate highway number.")