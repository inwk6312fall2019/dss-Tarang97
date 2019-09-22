# Two words are a “reverse pair” if each is the reverse of the other. Write a program
# that finds all the reverse pairs in the word list.

import bisect

def word_list(file):
    fin = open(file)
    li = []
    for line in fin:
        word = line.strip()
        li.append(word)
    return li

def in_bisect(word_list, word):
    i = bisect.bisect_left(word_list,word)
    if i == len(word_list):
        return False
    return word_list[i] == word

def reverse_pair(lst):
    list_of_pairs = []
    for word in lst:
        if in_bisect(lst, word[::-1]):
            pair = (word,word[::-1])
            list_of_pairs.append(pair)
    return list_of_pairs

lst = word_list('words.txt')
print(reverse_pair(lst))

# word_list() takes word from words.txt and appending it in a list then in_bisect() function
# sorts the list right from the first element enters in word_list. The bisect_left() bisects
# the word from the word_list and compares if the length of the word_list is equals to bisected 
# word. Then after fetching and bisecting, the original word is reversed using slice operator
# and appended in new list For example: [('aah','haa')]. the Iterations continued until the 
# the for loop reads the entire words.txt file and returns each reverse pair of each word.