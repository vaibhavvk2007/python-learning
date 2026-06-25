# list=[1,2,3,4,5]
# print(type(list))

# print(list[0])
# print(list[2])

# list=[100,99,"vaibhav",True,99.99,9.69]
# print("list can have all the datatypes of elements in it but it's type is always",type(list))
# print(type(list))
# print(list[len(list)-2])
# print(type(list[2]))            #to get the type of an single element

# if 100 in list:
#     print("yes")
# else:
#     print("no")

# if "vb" in "vaibhav":
#     print("yes")
# else:
#     print("no")

# print(list)
# print(list[0:len(list)])
# print(list[1:])
# print(list[1:4])
# print(list[:3])
# print(list[1:5:2])
# print(list[1::2])

# list=[i for i in range(10)]
list=[i*i for i in range(10)]
print(list)
lst=[i*i for i in range(10) if i%2==0]
print(lst)

names=["harry","vaibhav","code","with","me"]
namesWith_A=[item for item in names if(len(item)>4)]
print(namesWith_A)