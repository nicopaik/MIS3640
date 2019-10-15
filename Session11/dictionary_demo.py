def histogram(s):
    d = dict()
    for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
        print(d)
    return d
h = histogram('Bookkeeper')
print(h)
