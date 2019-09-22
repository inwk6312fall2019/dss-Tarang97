# If you did Exercise 10.7, you already have a function named has_duplicates
# that takes a list as a parameter and returns True if there is any object that
# appears more than once in the list.

#has_duplicate() using lists
lst = list(input('Enter any string: '))
print(lst)
def has_duplicates(lst):
    i = 0
    count = 0
    while i < len(lst) - 1:
        if lst[i] == lst[i + 1]:
            count += 1
            i += 2
            return True
        else:
            count = 0
            i += 1
    return False
print(has_duplicates(lst))

# has_duplicate() using dictionary
def has_duplicate(lst):
    dictionary = dict()
    for word in lst:
        if word in dictionary:
            return True
        dictionary[word] = True
    return False
print(has_duplicate(lst))