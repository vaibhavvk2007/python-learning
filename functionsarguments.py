# def average(a,b):
#     print("The average is: ",(a+b)/2)

# average(4,6)

# def average(a=5,b=9):
#     print("The average is: ",(a+b)/2)
# #In python the arguments passed outside the function eventhough the arguments are passed before
# average(4,6)


#Default Arguments
# def name(fname, mname="Jhon",lname="Whatson"):
#     print("Hello, ",fname,mname,lname)

# name("peter")

#Keyword Arguments
def name(fname, mname="Jhon",lname="Whatson"):
    print("Hello, ",fname,mname,lname)

name(mname="parker",fname="peter")
