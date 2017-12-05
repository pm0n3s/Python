'''Write a function that simulates tossing a coin 5,000 times. 
Your function should print how many times the head/tail appears.'''
import random

def cointoss():
    heads = 0
    tails = 0
    for i in range(1, 5001):
        l = ""
        toss = random.randint(1, 2)
        if toss == 1:
            heads += 1
            l = "It's HEADS!"
        else:
            tails += 1
            l = "It's TAILS!"
        print "Attempt #{}: Throwing a coin... {} ... Got {} head(s) so far and {} tail(s) so far".format(i, l, heads, tails)
cointoss()
