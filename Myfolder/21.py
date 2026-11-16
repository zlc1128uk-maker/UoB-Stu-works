grade = int(input("Enter your grade: "))

if grade >= 70 and grade <= 100:
    print("1st")
elif grade >= 60:
    print("2.1")
elif grade >= 50:
    print("2.2")
elif grade >= 40:
    print("3rd")
elif grade >= 0:
    print("F")
else:
    print("Invalid grade")