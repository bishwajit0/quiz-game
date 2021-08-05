import random
import questions
from random import choice
from questions import *

q = str.lower(input("Do you wanna play? "))

if q != "yes":
   quit()

print("Okay lets play!")
score = 0

random_item = random.choice(questions)
a = str(input(random_item))
if a in answers:
    print("Your answer is correct!")
    score += 1
else:
    print("Sorry, wrong answer!")


random_item = random.choice(questions)
a = str(input(random_item))
if a in answers:
    print("Your answer is correct!")
    score += 1
else:
    print("Sorry, wrong answer!")


random_item = random.choice(questions)
a = str(input(random_item))
if a in answers:
    print("Your answer is correct!")
    score += 1
else:
    print("Sorry, wrong answer!")

random_item = random.choice(questions)
a = str(input(random_item))
if a in answers:
    print("Your answer is correct!")
    score += 1
else:
    print("Sorry, wrong answer!")

random_item = random.choice(questions)
a = str(input(random_item))
if a in answers:
    print("Your answer is correct!")
    score += 1
else:
    print("Sorry, wrong answer!")


print("You got " +  str(score) + " questions correct!")
print("You got " +  str((score/5)*100) + "%.")