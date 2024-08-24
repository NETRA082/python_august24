#program to find sum of digits of a number
input_num = int(input("Enter a number to find sum of digits:"))
sum_digits = 0
while input_num > 0:
      digit = input_num % 10
      sum_digits += digit
      input_num = input_num // 10 
print("sum o f digits is",sum_digits)