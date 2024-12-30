def odd_or_even(n):
    return 'even' if n%2==0 else 'odd'
n= int(input("Enter the value : "))
print(f'{n} is ',odd_or_even(n))
