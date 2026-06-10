            #Variables and Data Types

            #everything in python is an object and has a data type


a=1.1
print(a)
b="vaibhav"
print(b)
c=True
print(c)
print("a+c=",a+c)
print("type of a is",type(a))
print("type of c is",type(c))

d=complex(2,3)
print("d=",d)
print("type of d is",type(d))

list=[1,2,3,4,5,[6,7,8],(9,10,11),{"name":"vaibhav","age":20}]
print("list=",list)
print("type of list is",type(list))

list.pop(2)
print("list after popping element at index 2=",list)
 
tuple=(1,2,3,4,5)
print("tuple=",tuple)
print("type of tuple is",type(tuple))

dict={"name":"vaibhav","age":20}
print("dict=",dict)
print("type of dict is",type(dict))