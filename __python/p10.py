#program to print Math table of a number.
number=int(input("Enter a number:"))
for i in range(1,11):
    print('%02d * %02d = %03d'%(number,i,number*i))