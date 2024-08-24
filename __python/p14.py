#program to find biggest(smallest) digit in a number.
input_num = int(input("Enter a number to find biggest digit in a number:"))
biggest_digit = 0
while input_num > 0:
       digit = input_num % 10
       if  digit > biggest_digit:
          biggest_digit = digit
       input_num = input_num // 10
print("the biggest digit in a number is",biggest_digit)