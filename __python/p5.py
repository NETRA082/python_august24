#Accept average score from the student of his exam and print his result as follows:
#0 to 49 is fail
# 50 to 74 is second class
#75 to 90 is first class
# 90 to 100 is distinction
#also check for invalidation

Student_result=int(input("enter the result of the student:"))
if Student_result > 100 or Student_result < 0:
    print("invalid input")
elif Student_result > 90 and Student_result < 100:
    print(" the result is distinction")
elif Student_result > 75 and Student_result < 90:
    print(" the result is first class")
elif Student_result > 50 and Student_result < 75:
    print("the result is second class")
else:
    print(" the result is fail")

