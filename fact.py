def fact(n):
    fact=1
    for i in range (1,n+1):
        fact*=i
    return fact
n=5
print(f'Factorial of {n} is ',fact(n))
