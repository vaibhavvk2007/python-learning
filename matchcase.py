# import os

# print("Hello world")
# print(os.getcwd())

            #switch case 

# x=int(input("Enter a number: "))
# match x:
#     case 0:
#         print("x is zero")
#     case value if value<0:
#         print("x is negative") 
#     case value if value>0:
#         print("x is positive")

a=input("Enter an integer or string:")

match a:
    case _ if a.isdigit():
        print("a is an integer")
    case str():
        print("a is string")
