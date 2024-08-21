#program to check if user given year is a Leap year.

year=int(input("Enter a year to check a given is a Leap year:"))
if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0 ):
    print(year,"is a Leap year")