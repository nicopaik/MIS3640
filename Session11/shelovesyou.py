def histogram(s):
    d = dict()
    for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
        print(d)
    return d

def histogram (h):
    for letter in h:
        print(letter, h[letter])

with open('session11/she_loves_you.txt') as f:
    lyrics = f.read().split()
    print(lyrics)

beatles = histogram(lyrics)
print_hist(beatles)
