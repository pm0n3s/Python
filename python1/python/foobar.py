'''Write a program that prints all the prime numbers and all the perfect squares 
for all numbers between 100 and 100000.

For all numbers between 100 and 100000 test that number for whether it is prime 
or a perfect square. If it is a prime number print "Foo". If it is a perfect square 
print "Bar". If it is neither print "FooBar". Do not use the python math library for 
this exercise. For example, if the number you are evaluating is 25, you will have 
to figure out if it is a perfect square. It is, so print "Bar".'''

for num in range(100, 100000):
    for i in range(2,num):
        if i * i == num:
            print("Bar")
        elif (num % i) == 0:
            print("FooBar")
            break
    else:
        print("Foo")