
names = ['Demi', 'Victoria', 'Carmen', 'Myat', 'Nico']
boys = ['Shaun', 'Brian', 'Krishna', 'Patrick']

print(names+boys)
print(names.extend(boys)) #old list changes
print(names.append(boys))

def capitalize_all(t):
    result = []
    for word in t:
        result.append(word.capitalize())

    return result
names = ['nico', 'myat', 'carmen']

print(capitalize_all(names))

def only_upper(t):
    res = []
    for s in t:
        if s.isupper():
            res.append(s)
    return res

animals = ['dog', 'cat', 'BIRDS', 'Sheep']
print(only_upper(animals))

print(names)

names.pop(2) #Delete carmen

def cumsum(t):

