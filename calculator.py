a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
opt=input("Enter your operation: ")
if opt=='+':
    result=a+b
elif opt=='-':
    result=a-b
elif opt=='*':
    result=a*b
elif opt=='/':
    result=a/b
elif opt=='//':
    result=a//b
elif opt=='**':
    result=a**b
else:
    result="invalid input or operator"

print("Result: ",result)