fin = open('words.txt')

# calculate_difference() will calculate the difference between the letter which are not same
# in both the words. If the difference is found, it reiterates using for loop for every letter and
# returns the difference as an integer.
def calculate_difference(word1, word2):
    assert len(word1) == len(word2)
    diff = 0
    for x,y in zip(word1,word2):
        if x!=y:
            diff += 1
    return diff

# is_anagram() will take a single text from 'words.txt', sorts it and lower the cases and 
# append the original word in the list which will be the default value of sorted_dict() values;
# but, the sorted_word will be in sorted_dict() dictionary along with its value.
def is_anagram(text):
    sorted_dict = dict()
    for line in text:
        original_word = line.strip()
        sorting_word = ''.join(sorted(list(original_word.lower()))) 
        sorted_word = sorting_word
        sorted_dict.setdefault(sorted_word, []).append(original_word)
    
    anagrams = []

# This for loop will take key and value from sorted_dict() using dict.items().
# the length of no. of words spelled with those letters will be counted and will be stored in 'l'.
# If length > 1, then (count of words formed, key(original word) , value (The words created with letters))
# will append in anagrams[] list.

    for k,v in sorted_dict.items():
        l = len(v)
        if l > 1:
            anagrams.append((l,k,v))
    return anagrams

def metathesis_pairs(text):
    anagrams = is_anagram(text)

    maps = []

    for lng, letter, ana in anagrams:
        for i in range(len(ana)):
            for j in range(i+1, len(ana)):
                if calculate_difference(ana[i], ana[j]) == 2:
                    maps.append([ana[i], ana[j]])
    return maps

metathesis_pairs = metathesis_pairs(fin)
print(metathesis_pairs)

#In metathesis_pairs(), it will take the text from which is simulated from is_anagram(),
# then for loop will go through the length and the letter from anagrams list.
# The second for loop will takes the length of anagram which is simulated from is_anagram()
# and that length will be the range for iterations. The third for loop will increase the 'i' by 1
# then the length of anagram which is simulated from is_anagram() will be the range for iterations for 'j'
# The calculate_difference() will returns the difference and if it is equals to '2' then it will append
# in maps[] list as ['bate','beta'].
# The transformation of another word depends on the difference we get from calculate_difference() function
# and what is_anagram() function does to words by reversing and sorting them.
# If we look each and every iterations carefully, then we'll know that metathesis_pairs are
# generated through the length of is_anagrams() function and the 'for' loops to check pairs for
# forming words. 