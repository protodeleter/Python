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