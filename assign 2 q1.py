# Write a program which takes 5 inputs from user for different subject’s
# marks, total it and generate mark sheet using grades ?
print("Enter your 5 subjects marks out of 100 one at a time")
subject1 = float(input("Enter marks of subject1: "))
subject2 = float(input("Enter marks of subject2: "))
subject3 = float(input("Enter marks of subject3: "))
subject4 = float(input("Enter marks of subject4: "))
subject5 = float(input("Enter marks of subject5: "))
add = subject1 + subject2 + subject3 + subject4 + subject5 
avg = add/5
if(avg>=90):
    print("percentage = " + str(avg))
    print("grade = A+")
elif(avg>=80):
    print("percentage = " + str(avg))
    print("grade = A")
elif(avg>=70):
    print("percentage = " + str(avg))
    print("grade = B")
elif(avg>=60):
    print("percentage = " + str(avg))
    print("grade = C")
elif(avg>=50):
    print("percentage = " + str(avg))
    print("grade = D")  
else:
    print("percentage = " + str(avg))
    print("grade = FAIL")