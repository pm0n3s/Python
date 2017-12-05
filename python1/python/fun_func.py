'''Odd/Even:
Create a function called odd_even that counts from 1 to 2000. As your loop 
executes have your program print the number of that iteration and specify 
whether it's an odd or even number.'''

def odd_even():
    for i in range(1, 2001):
        if i % 2 == 0:
            print "Number is {}. This is an even number.".format(i)
        else:
            print "Number is {}. This is an odd number.".format(i)
odd_even()

'''Multiply:
Create a function called 'multiply' that iterates through each value in a list 
(e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied 
by 5.
The function should multiply each value in the list by the second argument. For 
example, let's say:'''

def multiply(a, b):
    for i in range(0, len(a)):
        a[i] *= b
    return a

a = [2,4,10,16]

b = multiply(a, 5)
print b

'''Hacker Challenge:
Write a function that takes the multiply function call as an argument. Your new 
function should return the multiplied list as a two-dimensional list. Each internal 
list should contain the 1's times the number in the original list.'''

def layered_multiples(arr):
    new_array = []
    for x in range(0, len(arr)):
        new_list = []
        for y in range(0, arr[x]):
            new_list.append(1)
        new_array.append(new_list)
    return new_array

x = layered_multiples(multiply([2,4,5],3))
print x
