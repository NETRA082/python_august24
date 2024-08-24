#program to find 2nd smallest digit in a number
input_number=int(input("enter a number to find 2nd smallest digit in a number:"))
small_digit = smallest_digit = 9
temp_number = input_number
while input_number != 0:
    digit = input_number % 10
    input_number = input_number // 10
    if smallest_digit>digit:
        small_digit=smallest_digit
        smallest_digit=digit
    elif digit < small_digit :
        small_digit = digit
print(f'2nd smallest digit in {temp_number} is {small_digit}')