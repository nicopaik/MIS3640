"""
age = int(input('Please enter your age:'))

print(f"Your age is {age}.")

if age >=18:
    print("You are an adult.")
elif age >= 10:
    print("You are a teenager")
else:
    print("You are a kid.")

def compare(varA, varB:)
    if isintance(varA, str) or isinstance(var8, str):
        print('string involved')
    else:
        if varA> varB:
            print('bigger')
        elif var

    Given an int n, return the absolute difference between n and 21, 
    except return double the absolute difference if n is over 21.
    
def diff21(n)
    if n<=21:
        return abs(n-21)
    else:
        return abs(n- 21) * 2
    

print(diff21(19)) # 2
print(diff21(10)) # 11
print(diff21(21)) # 0       
"""

def countdown(n):
    import time
    time.sleep(1)

    if n <= 0:
        print("Blastoff")
    else:
        print(n)
        countdown(n - 1)

countdown(5)