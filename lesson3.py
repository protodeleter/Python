import math


def func1():
    lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

    newlst=[val for val in lst if val % 2 == 0]

    print(newlst)
def func2(lst1,lst2):

    newlst =  [abs(lst1[i]-lst2[i]) for i in range(len(lst1))]
    return newlst


# Answer exercise 3
# cuts the letter "s" from the string
#

# Answer exercise 4
# Creates a list of words from string separated by comma

def pipe_fix(nums):
    return [x for x in range(nums[0], nums[-1] + 1)]


def invert(lst):
    return [-x for x in lst ]

def monkey_count(n):
    return [i for i in range(1, n + 1)]

# Fixed Tests
# Positive Constant
#  (4 of 4 Assertions)
# Negative Constant
#  (4 of 4 Assertions)
# Completed in 0.11ms
def seqlist(first, c, l):
    return [first + i * c for i in range(l)]


# Exersize 10
# Fucntion filters the list
# if list item is negative int it reverses its digits preserving the negative value
#


def is_prime(num):
    return num > 1 and not any(num % x == 0 for x in range(2, num))

print(is_prime(100))

def is_funny(string):
    return len([s for s in string if s != 'h' and s != 'a']) == 0

print(is_funny('haha'))