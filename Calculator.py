#this is a calculator
firstValue=int(input("Enter the First Value and press Enter:"))
operator=input("Enter one of the signs[+,-,*,/]:")
SecondValue=int(input("Enter the Second Value and press Enter:"))

if (operator=='+'):
    print("After Adding ",firstValue," and ",firstValue," we get-",firstValue+SecondValue)

if (operator=='-'):
    print("After Subtracting ",firstValue," and ",firstValue," we get-",firstValue-SecondValue)

if (operator=='*'):
    print("After Multiplying ",firstValue," and ",firstValue," we get-",firstValue*SecondValue)

if (operator=='/'):
    print("After Dividing ",firstValue," and ",firstValue," we get-",firstValue/SecondValue)
