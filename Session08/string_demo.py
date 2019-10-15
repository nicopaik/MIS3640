team = 'New England Patriots'
# letter = team[0]
# print(letter)

# print(team[1]) # N e

#print(len(team)) #20
# print(team[-1]) #S
# print(team[-20])N

# index = 0
# while index < lens(team):
#         letter = team[index]
#         print(letter)
#         index = index + 1

# for letter in team:
#     print(letter)

# print(letter)

# prefixes = 'JKLMNOPQ'
# suffix = 'ack'
# for letter in prefixes:
#     if letter == '0' or letter == 'Q'
#     print(letter+'u' + suffix)
#     else:
#     print(letter + suffix)


team = 'New England Patriots'

print(team[0:11])
print(team[12:20])

print(team[0:20:2]) #by 2's

#team[12:20] = 'Seahawks'

# new_team = team[:12] +
# 'Giants'
# print(new_team)
# print(team)

def count(s, letter):

    counter = 0
    for c in s:
        if c == letter:
            counter += 1
    return(counter)

print(count(team, 'a'))
print(count(team, 'e'))