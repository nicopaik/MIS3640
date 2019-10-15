 def histogram(s):
    d = dict()
     for letter in s:
        if letter not in d:
            d[letter] = 1
        else:
            d[letter] += 1
     return d

 print(histogram('Bookkeeper'))

def histogram(s):
    d = dict()
    for c in s:
        d[c]=d.get(c, 0) + 1
    return d

 print(histogram('bookbookkeepp'))

def print_hist(h):
    for c in h:
        print(c, h[c])
        
h = histogram('Massachusetts')
 print_hist(h)
