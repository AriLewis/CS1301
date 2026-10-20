password = input("Please Enter Your Password: ")
strong_p = " "
for char in password:
    if char == 'o':
        strong_p += '0'
    elif char == 'i':
        strong_p += '1'
    elif char == 'a':
        strong_p += '@'
    elif char == 'e':
        strong_p += '3'
    elif char == 'A':
        strong_p += '4'
    elif char == 'B':
        strong_p += '8'
    elif char == 's':
        strong_p += '$'
    else:
        strong_p += char
print(f"your new strong password is: {strong_p}!")
