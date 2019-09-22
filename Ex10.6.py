# Two words are anagrams if you can rearrange the letters from 
# one to spell the other. Write a function called is_anagram 
# that takes two strings and returns True if they are anagrams. 
def is_anagram(a,b):
    for i in a:
        if i in b:
            return True
        else:
            return False

a = input('Enter 1st string: ')
b = input('Enter 2nd string: ')
print(is_anagram(a,b))