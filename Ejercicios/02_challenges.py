"""
FizzBuzz" is a classic programming challenge that involves printing numbers from 1 to 100, but for multiples of 3, you print "Fizz" instead of the number, for multiples of 5, you print "Buzz", and for numbers that are multiples of both 3 and 5, you print "FizzBuzz" without function. The following code implements this challenge in Python

"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)