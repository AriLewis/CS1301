while True:
    string = input("Please Enter Your String: ")

    if string in ("Quit", "quit", "q"):
        break

    reverse = ""
    for i in range(len(string) - 1, -1, -1):
        reverse += string[i]

    print(f"Reversed: {reverse} ")