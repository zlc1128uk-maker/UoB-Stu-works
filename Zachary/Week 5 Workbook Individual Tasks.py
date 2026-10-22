#Week 5 Workbook Individual Tasks

name = "Zachary"
age = 22

Q1 = (f"My name is {name}\n{name} is {age} years old\n{name} likes to eat japanese and italian food\n{name} comes from Singapore\n{name} wants to study computer science\n{name} is sleepy.")
Q2 = "Hello World!"
Q3 = "Welcome to my Python Programming!"
Q4 = 'Albert Einstein once said, "Imagination is more important than knowledge."'
Q5 = 'Tom said, "I have always liked to hear \'I am the best\' as often as possible".'

from datetime import datetime                                    #Time Library allows us to use the current time and date function

Q6 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")                #Sets formatting for time module to remove decimal seconds

questions = {
    "1": Q1,
    "2": Q2,
    "3": Q3,
    "4": Q4,
    "5": Q5,
    "6": Q6,
}                                                                #Dictionary to store all 6 questions into an input

choice = input("Input your current question number: ")

if choice in questions:
    print(questions[choice])                                     #Control Flow Statement to display the correct question from dictionary
else:
    print("Please enter a number from 1 to 6.")