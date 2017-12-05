'''Create a program that prints a multiplication table in your console.'''

print "x   1   2   3   4   5   6   7   8   9  10  11  12"

for i in range(1, 13):
    print i,
    for n in range(1, 13):
        x = i * n
        if x < 10:
            print "  " + str(i * n),
        elif x < 100:
            print " " + str(i * n),
        elif x < 150:
            print str(i * n),
        if n == 12:
            print '\n'