# Read the documentation of the dictionary method setdefault and 
# use it to write a more concise version of invert_dict.

#Histogram
def histogram(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d
h = histogram('brontosaurus')
print(h)

#Here is a function that inverts dictionary
def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse
hist = histogram('parrot')
print(hist)
inverse = invert_dict(hist)
print(inverse)