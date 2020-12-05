#Alper Tunahan Öztürk

from decimal import Decimal
import random as rnd


# Calculation of the letter of grades.

def CalcPass(dict):
    grades = []
    for value in dict.values():
        grades.append(value)

    lastGrade = (grades[0] * 0.3 + grades[1] * 0.5 + grades[2] * 0.2)
    lastGrade = Decimal("%.2f" % lastGrade)

    print("Your course grade is : ", lastGrade)

    if lastGrade > 90:
        print("Letter note of the course is AA.")
    elif lastGrade < 90 and lastGrade >= 70:
        print("Letter note of the course is BB.")
    elif lastGrade < 70 and lastGrade >= 55:
        print("Letter note of the course is CC.")
    elif lastGrade < 50 and lastGrade >= 30:
        print("Letter note of the course is DD.")
    else:
        print("Letter note of the course is FF. You have failed the class.")



# If the user cannot login within 3 tries the program will execute by itself.
# Use alpertunahan as name, and ozturk for surname.
check = False

for i in range(3):

    name = input("Please enter your name (if you have two names please enter without space) : ")
    name = name.lower()

    surname = input("Please enter your surname  : ")
    surname = surname.lower()

    if name == "alpertunahan" and surname == "ozturk" :
        print("Welcome to the system!")
        check = True
        break
    else:
        print("The informations are wrong, please try again.")



howMany = None
courses = ["stat363", "stat303", "math260", "fde100", "stat203"]

# Grades of courses
# Working on how to stop the randomazing every time code runs

gradesOf363 = {"Midterm" : rnd.randint(1,100), "Final" : rnd.randint(1,100), "Project" : rnd.randint(1,100)}
gradesOf303 = {"Midterm" : rnd.randint(1,100), "Final" : rnd.randint(1,100), "Project" : rnd.randint(1,100)}
gradesOf203 = {"Midterm" : rnd.randint(1,100), "Final" : rnd.randint(1,100), "Project" : rnd.randint(1,100)}
gradesOf260 = {"Midterm" : rnd.randint(1,100), "Final" : rnd.randint(1,100), "Project" : rnd.randint(1,100)}
gradesOf100 = {"Midterm" : rnd.randint(1,100), "Final" : rnd.randint(1,100), "Project" : rnd.randint(1,100)}



# Overall results of courses.

if check == True:
    howMany = int(input("How many courses you want to take between 3 and 5 : "))
    if howMany < 3 :
        print("You can not take less than 3 courses.")
    elif howMany > 5 :
        print("You can not take more than 5 courses.")
    else:
        print("Which course you want to take (Please enter the name of te course):\n", courses)
        
        for i in range(howMany):
            course = input(" = ")
            if course == "stat363":
                CalcPass(gradesOf363)
            
            elif course == "stat303":
                CalcPass(gradesOf303)
            
            elif course == "stat203":
                CalcPass(gradesOf203)
            
            elif course == "math260":
                CalcPass(gradesOf260)
            
            elif course == "fde100":
                CalcPass(gradesOf100)
            else:
                print("There is no such that course.")
