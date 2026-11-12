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



"""
Anagrama 
"""

def is_anagram(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    
    # Sort the characters of both strings and compare
    return sorted(str1) == sorted(str2)

print(is_anagram("listen", "silent"))  # True
print(is_anagram("hello", "world"))  # False