# Write a function that reads the file words.txt and 
# builds a list with one element per word. 
# Write two versions of this function, 
# one using the append method and the other using the idiom t = t + [x]. 
# Which one takes longer to run? Why?


def version1(fin):
    lst1 = []
    for word in fin:
        char = word.strip()
        lst1.append(char)
    return lst1

def version2(fin):
    lst2 = []
    for word in fin:
        letter = word.strip()
        lst2 = lst2 + [letter]
    return lst2
fin = open('words.txt')
print(version1(fin))
print(version2(fin))

# First version returns the list quickly
# but the second version returns empty List []. Don't Understand that one.