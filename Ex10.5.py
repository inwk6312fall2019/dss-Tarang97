# Write a function called is_sorted that takes a list as a parameter 
# and returns True if the list is sorted in ascending order and False otherwise.

lst = list(input('Enter anything: '))
print(lst)
def is_sorted(lst):
    if lst != lst.sort():
        lst.sort()
        return True
    return False
print(is_sorted(lst))
print(lst)
