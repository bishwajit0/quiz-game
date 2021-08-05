import random
import questions
from random import choice
from questions import *

q = str.lower(input("Do you wanna play? "))

if q == "yes":
    random_item = random.choice(questions)
    a = str(input(random_item))
    score = 0
    if a in answers:
        print("Your answer is correct!")
        score += 1
    else:
        print("Sorry, wrong answer!")
else:
    quit()
    