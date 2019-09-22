# Write a function called nested_sum that takes a list of lists of 
# integers and adds up the elements from all of the nested lists. 
# For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21

from functools import reduce

lst = [10,11,12,13,14,15,16,17,18,19,20]
def add(x,y):
    return x+y
print(reduce(add, lst))

List = [10,11,12,13,14,15,16,17,18,19,20,[21,22,23,24,[25,26,27]]]
def nested_sum(x,y):
    return x+y
print(reduce(add, List[-1][-1]))