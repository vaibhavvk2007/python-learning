#Tuples and it's elements cannot be changed and if needed then the tuple should be converted to a list then made changes and then again change it to a tuple as there is no in built methods to changes it.
#Here is an Example
#inshort Tuples Are immutable and Lists are mutable
countries=["India","Russia","Ukarine","Usa","china","Japan"]
temp=list(countries)
temp.append("switzerland")
temp.pop(3)
temp[3]="Finland"
countries=tuple(temp)
print(countries)


tup1=(1,2,3,4,100,6,7,8,9)
tup2=(10,11,12,13,14,15)
tuple=tup1+tup2
print(tuple)
print(tuple.count(10))
print(tuple.index(4))
print(tuple.index(7))