p_number = int(input("Please Enter your phone number: "))

l_num = p_number % 10000
p_number = p_number // 10000

pre = p_number % 1000
p_number = p_number // 1000

area_code = p_number

print(f"Your phone number: ({area_code}) {pre}-{l_num}")

