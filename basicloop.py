# Print all integers from 0 to 150.
for x in range(0, 151):
    print(x)

# Print all the multiples of 5 from 5 to 1,000
for x in range(5, 1001, 5):
    x <= 1000
    print(x)

# Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
for i in range(1, 101):
    if i % 5 == 0:
        print('coding')
    if i % 10 == 0:
        print('coding dojo')

# Add odd integers from 0 to 500,000, and print the final sum.
min = 0
max = 500000
Oddtotal = 0
for int in range(min, max + 1):
    if (int % 2 != 0):
        print("{0}".format(int))
        Oddtotal = Oddtotal + int

print("The Sum of Odd int from {0} to {1} = {2}".format(min, max, Oddtotal))


# Countdown by Fours - Print positive numbers starting at 2018, counting down by fours.

for x in range(2018, 0, -4):
    print(x)


# Flexible Counter - Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)
lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum + 1):
    if x % mult == 0:
        print(x)