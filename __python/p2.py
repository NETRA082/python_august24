#Read the number from user and check if it is an Even or not.
# To read data from the console,we can use input().However the input()always reads onlya string as usual with all other languages.
#we must 1st cast(convert)the string into a number(specifically int)
#the input(),not just reads a string but also can print a string

my_number=int(input('Enter a number to check if it is Even or not:'))
print(type(my_number))
if my_number%2==0:
    print(my_number,'is Even')
else:
    print(my_number,'is npot Even')