#program to find sum of Even(odd) digits in a number
input_num = int(input("Enter a number to find sum of Even digits in a number:"))
sum_Even = 0
while input_num > 0:
    digit = input_num % 10
    if input_num % 2 == 0:
        sum_Even = sum_Even + digit
    input_num = input_num // 10
print("The sum of Even digits in a number is:",sum_Even)
