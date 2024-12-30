number = int(input("Enter a number : "))
length = len(str(number))
power = sum (int(digit) ** length for digit in str(number))
if power == number :
    print(f"{number} is an armstrong number")
else :
    print(f"{number} is not an armstrong number")