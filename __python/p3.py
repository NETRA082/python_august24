#Accept a number as input,say X and define a logic to get the output say Y.The Input can br only 0 or 1 and the output must be 1 if input is 0 and viceversa.
x=int(input("Enter the input number 0 or 1 only:"))
if x!=1 and x!=0:
    print("Invalid input")
else:
    y=1-x
    print(f'Input number={x},Output number={y}')



