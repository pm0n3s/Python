'''Create a dictionary containing some information about yourself. 
The keys should include name, age, country of birth, favorite language.'''

me = {
    "name": "Patrick",
    "age": 26,
    "country": "USA",
    "favorite language": "Python"
}

'''Write a function that will print something like the following as it executes:

My name is Anna
My age is 101
My country of birth is The United States
My favorite language is Python

There are two steps to this process, building a dictionary and then gathering all 
the data from it. Write a function that can take in and print out any dictionary 
keys and values.

Note: The majority of data we will manipulate as web developers will be hashed in 
a dictionary using key-value pairs. Repeat this assignment a few times to really 
get the hang of unpacking dictionaries, as it's a very common requirement of any 
web application.'''

def read_dict(d):
    for key, value in d.iteritems():
        print "My {} is {}".format(key, value)

read_dict(me)