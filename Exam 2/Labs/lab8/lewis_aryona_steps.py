'''
Aryona Lewis
converting feet to steps
'''
def feet_to_steps(feet):
    steps = feet / 2.5
    return int(steps)


def main():
    feet = float(input("Please enter the distance travelled in feet: "))
    steps = feet_to_steps(feet)
    print(f"{steps} steps")


main()