import math

def gradeCalculator (score):
    if (score >= 90):
        print("Your grade is an 'A'")
    elif (score >= 80):
        print("Your grade is an 'B'")
    elif (score >= 70):
        print("Your grade is an 'C'")
    elif (score >= 60):
        print("Your grade is an 'D'")
    else:
        print("Your grade is an 'F'")
        

while(True):
    score = float(input("Enter your grade: "))
    score = math.ceil(score)
    gradeCalculator(score)
