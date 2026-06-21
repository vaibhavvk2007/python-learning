# Functions are something that we need multiple times in a program that is a single code snippet used multiple times
# a=8
# b=6
# gmean=(a*b)/(a+b)
# print(gmean)

# c=17
# d=54
# gmean1=(c*d)/(c+d)
# print(gmean1)

def calculategmean(a,b):
    mean=(a*b)/(a+b)
    print (mean)

def isgreater(a,b):
    if(a>b):
        print("first number is greater")
    else:
        print("Second number is greater")


a=8
b=6
# gmean=(a*b)/(a+b)
# print(gmean)
calculategmean(a,b)
isgreater(a,b)
c=8
d=54
# gmean1=(c*d)/(c+d)
# print(gmean1)
calculategmean(c,d)
isgreater(c,d)