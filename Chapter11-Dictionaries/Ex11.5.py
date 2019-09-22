# Two words are “rotate pairs” if you can rotate one of them and 
# get the other (see rotate_word in Exercise 5).

def rotate_letter(lett,n):
    if lett.isupper():
        start = ord('A')
    elif lett.islower():
        start = ord('a')
    else:
        start = ord(lett)
    
    lett_chr = ord(lett)
    diff = start + ((lett_chr-start) + n) % 26

    return chr(diff)
# print(rotate_letter('A',3))
def rotate_word(word,n):
    new_word = ''

    for lett in word:
        new_lett = rotate_letter(lett,n)
        new_word += new_lett
    return new_word

fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)
        print(rotate_word(word, 2),"\n")