#program to find odd placed digits  in a number.
input_number=int(input("Enter a number to find odd placed digits in a number:"))
odd_digits=0
while input_number > 0:
    digits = input_number % 10
    if digits % 2 != 0:
        odd_digits = odd_digits * 10 + digits
    input_number = input_number // 10
print("Odd placed digits in a number is:",odd_digits)
    

