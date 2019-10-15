L = [
    ['Apple', 'Google', 'Microsoft'], # 0
    ['Java', 'Python', ['Ruby','On Rail'], 'PHP'], # 1
    ['Adam', 'Bart', 'Lisa']    # 2
]

len(L)

AFC_east = ['New England Patriots', 'Buffalo Bills', 'Miami Dolphins', 'New York Jets']
print('Buffalo Bills' in AFC_east)


# for team in AFC_east:
#     for letter in team:
#         print(letter)

numbers = [2019, 10, 8, 3, 43]

# for i in range(len(numbers)):
#     numbers[i]=numbers[i] * 2

# print(numbers) # everything is doubled

for number in numbers: #Stays the same, # the previous one
    number = number * 2

print(numbers)


my_list = ['spam', 1, ['New England Patriots', \
                       'Buffalo Bills', 'Miami Dolphins', \
                       'New York Giants'], \
           [1, 2, 3]]

print(len(my_list))

a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print (c) #same line

t = ['a', 'b', 'c', 'd', 'e', 'f']
print(t[1:3])
print(t[0:4])
print(t[3:6])
print(t[::2]) # A , C , E :: is whole list, from the whole list go by 2 intervals
print(t[::-2]) #FDB

t = ['a', 'Victoria', 'd', 'e', 'f']

t[1] ='nico'
print(t)