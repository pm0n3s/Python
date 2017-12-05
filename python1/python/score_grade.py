'''Write a function that generates ten scores between 60 and 100. Each time a 
score is generated, your function should display what the grade is for a particular 
score. Here is the grade table:'''
import random

def grade_scorer():
    print "Scores and Grades"
    for grade in range(0, 10):
        r = random.randint(60, 100)
        print "Score: {};".format(r),
        if r < 70:
            print "Your grade is D"
        elif 69 < r < 80:
            print "Your grade is C"
        elif 79 < r < 90:
            print "Your grade is B"
        else:
            print "Your grade is A"

grade_scorer()
