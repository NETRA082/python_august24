#program to print the hallow square.
number_of_lines = int(input("Enter number of lines to draw the hallow square:"))
for i in range(1,number_of_lines+1):
    for j in range(1,number_of_lines+1):
        if j == 1 or j == number_of_lines or i==1 or i==number_of_lines:
            print("*",end =' ')
        else:
            print(' ',end =' ')
    print()

        