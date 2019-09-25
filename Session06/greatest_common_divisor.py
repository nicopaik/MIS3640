#3

def gcd(a, b):
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcd(b, a % b)

print(gcd(2, 12)) #2 

print(gcd(6, 12)) #6

print(gcd(9, 12)) #3

print(gcd(17, 12)) #1