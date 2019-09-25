def Fibonacci(n):
    if n==1 or n==2:
        return 1
    else:
        return Fibonacci(n-1)+Fibonacci(n-2) 

print(Fibonacci(1))

print(Fibonacci(2))

print(Fibonacci(10))

for i in range(1, 20, 1):
    print(Fibonacci(i))