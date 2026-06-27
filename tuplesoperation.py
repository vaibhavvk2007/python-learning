#Tuples and it's elements cannot be changed and if needed then the tuple should be converted to a list then made changes and then again change it to a tuple as there is no in built methods to changes it.
#Here is an Example
countries=["India","Russia","Ukarine","Usa","china","Japan"]
temp=list(countries)
temp.append("switzerland")
temp.pop(3)
temp[3]="Finland"
countries=tuple(temp)
print(countries)
