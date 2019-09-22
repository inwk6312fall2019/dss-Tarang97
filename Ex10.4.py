# Write a function called chop that takes a list, 
# modifies it by removing the first and last elements, 
# and returns None. For example:
# >>> t = [1, 2, 3, 4]
# >>> chop(t)
# >>> t
# [2, 3]

lst = [1,2,3,4,5,6]
print(lst)
def chop(lst):
    lst.pop(5)
    lst.pop(0)
print(chop(lst))
print(lst)