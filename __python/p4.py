#program to Accept 3 distinct number and find smallest among them

input_num1 = int(input('Enter first Number:'))
input_num2 = int(input('Enter second Number:'))
input_num3 = int(input('Enter third Number:'))
if input_num1 < input_num2 and input_num1 < input_num3:
  print(f'{input_num1} is smallest')
elif input_num2 < input_num3:
  print(f'{input_num2} is smallest')
else :
  print(f'{input_num3} is smallest')
