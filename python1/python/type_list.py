'''Write a program that takes a list and prints a message for each element in 
the list, based on that element's data type.

Your program input will always be a list. For each item in the list, test its data 
type. If the item is a string, concatenate it onto a new string. If it is a number, 
add it to a running sum. At the end of your program print the string, the number 
and an analysis of what the list contains. If it contains only one type, print that 
type, otherwise, print 'mixed'.'''

#varibales
l = ['magical unicorns',19,'hello',98.98,'world']
l_string, l_sum = "", 0
num, string = False, False

# sorting function
for i in l:
    if isinstance(i, int):
        l_sum += i
        num = True
    elif isinstance(i, str):
        l_string += i + " "
        string = True

#list type finction
if num and string:
    print "The list you entered is of mixed type"
    print "String: " + l_string
    print "Sum: " + str(l_sum)
elif num:
    print "The list you entered is of integer type"
    print "Sum: " + str(l_sum)
elif string:
    print "The list you entered is of string type"
    print "String: " + l_string
