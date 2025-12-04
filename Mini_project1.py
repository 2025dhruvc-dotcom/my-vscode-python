
# Mini Project - Student Report Card
name = input("Enter Student name: ")
roll = input("Enter Roll number: ")
maths = int(input("Enter Maths marks: "))
science = int(input("Enter Science marks: "))
english = int(input("Enter English marks: "))

#Calculations
total = maths + science + english
average = total / 3
average = round(average,2)

#Conditions
if average >= 40:
    result = "PASS"
else:
    result = "FAIL"

#Printing Report Card
print("\n ----- Student Report Card -----")
print("\n   --> Name   : ", name)
print("\n   --> Roll No: ", roll)
print("\n   --> Total  : ", total)
print("\n   --> Average: ", average)
print("\n   --> Result : ", result)
print("\n -------------------------------")





