#program to check if a number is perfect square
number=int(input("Enter a number to check if a number is perfect square:"))
if number >= 0:
    r=int(number**0.5)
if r**2==number:
    print(number,"is a perfect square")