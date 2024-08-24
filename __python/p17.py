#program to reverse a number
input_number=int(input("Enter a number to reverse:"))
reversed_number = 0
while input_number > 0:
    digit = input_number % 10
    reversed_number = (reversed_number * 10) + digit
    input_number = input_number//10
print(" the reversed number is:",reversed_number)
