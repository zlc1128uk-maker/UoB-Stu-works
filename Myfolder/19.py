student_id = input("Enter student ID: ")
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

mark1 = float(input("Enter mark 1: "))
mark2 = float(input("Enter mark 2: "))
mark3 = float(input("Enter mark 3: "))
mark4 = float(input("Enter mark 4: "))

time = input("Enter hour (0-23), or press Enter to skip: ")

if time == "":
    greeting = "Hello"
else:
    hour = int(time)

    if hour < 12:
        greeting = "Good morning"
    elif hour < 18:
        greeting = "Good afternoon"
    else:
        greeting = "Good evening"

print(greeting, first_name)
average = (mark1 + mark2 + mark3 + mark4) / 4
print("Average:", average)

highest = mark1
lowest = mark1

if mark2 > highest:
    highest = mark2
if mark2 < lowest:
    lowest = mark2

if mark3 > highest:
    highest = mark3
if mark3 < lowest:
    lowest = mark3

if mark4 > highest:
    highest = mark4
if mark4 < lowest:
    lowest = mark4

difference = highest - lowest

print("Highest mark:", highest)
print("Lowest mark:", lowest)
print("Difference:", difference)

if average >= 60:
    print("PASS")
else:
    print("FAIL")

if average >= 80:
    print("Excellent")
elif average >= 70:
    print("Well done")
