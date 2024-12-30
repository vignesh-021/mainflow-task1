a,b=0,1
n=int(input("Enter a value : "))
for i in range (n):
    print(a,end=" ")
    a,b=b,a+b
    