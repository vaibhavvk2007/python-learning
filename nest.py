num=int(input("Enter a number: "))
if num<0:
    print("The number is negative")
elif num>0:
    print("The number is positive")
    if (num<=10):
        print("The number is less than or equal to 10")
    elif (num<=20):
        print("The number is less than or equal to 20")
    else:
        print("the number is greater than 20")
else:
    print("The number is zero") 