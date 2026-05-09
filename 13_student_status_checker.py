print("=>>>>>>>>>> STUDENT STATUS CHECKER >>>>>>>><<=")

name = input("Enter name: ")
if len(name) == 0:
    print("Invalid name!")
    exit()

marks = float(input("Enter marks: "))
if marks < 0 or marks > 100:
    print("Invalid marks!")
    exit()
else:
    if marks >= 90:
        grade = 'A'
        status = "Pass"
    elif marks >= 80:
        grade = 'B'
        status = "Pass"
    elif marks >= 70:
        grade = 'C'
        status = "Pass"
    elif marks >= 60:
        grade = 'D'
        status = "Pass"
    else:
        grade = 'F'
        status = "Fail"

print(name, '|', marks, "| Grade:",grade,"| Status:",status)
