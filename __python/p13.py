#program to find count of a number
input_num = int(input("enter a number to find count of a number:"))
count_number = 0
while input_num > 0:
    digit = input_num % 10
    count_number = count_number + 1
    input_num = input_num // 10
print("count of a number is",count_number)
