fin = open('words.txt')

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

def longest_list_anagrams(text):
    anagrams = is_anagram(text)
    longest_list_anagrams = []

    for l,k,v in reversed(sorted(anagrams)):
        longest_list_anagrams.append((l,k,v))
    return longest_list_anagrams

longest_list_anagrams = longest_list_anagrams(fin)
print(longest_list_anagrams[:5])

# longest_list_anagrams() will take the anagrams from is_anagram() and gets the anagrams[] list
# then it will get reversed and sorted and then it will append in longest_list_anagrams[].