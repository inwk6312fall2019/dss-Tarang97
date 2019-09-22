# Write a function called cumsum that takes a list of 
# numbers and returns the cumulative sum; that is, 
# a new list where the ith element is the sum of 
# the first i+1 elements from the original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]

lst = [1,2,3,4,5,6,7,8,9]
def cumsum(lst):
    lstsum = []
    total_sum = 0
    for num in lst:
        total_sum += num
        lstsum.append(total_sum)
    return lstsum
print(cumsum(lst))
