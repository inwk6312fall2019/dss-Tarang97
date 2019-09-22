# Write a function that reads the words in words.txt and stores them as keys in a
# dictionary. It doesn’t matter what the values are. Then you can use the
# in operator as a fast way to check whether a string is in the dictionary.

def words_in_dictionary():
    word_list = dict()
    fin = open('words.txt')
    for line in fin:
        word = line.strip()
        if word not in word_list:
            word_list[word] = None
    return word_list
print(words_in_dictionary())

def word_finding(word):
    if word in words_in_dictionary():
        return True
    return False

word = input('Enter any string: ')
print(word_finding(word))