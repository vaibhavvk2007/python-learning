            #DAY32
# s1={1,2,3}
# s2={3,5,6}
# print(s1.union(s2))
# s1.update(s2)
# print(s1,s2)

cities={"Tokyo","Madrid","Berlin","Delhi"}
cities2={"Tokyo","Seoul","Kabul","Madrid"}

cities4={"Tokyo","Madrid"}

#1      cities3=cities.intersection(cities2)        # This returns a new set  
#       print(cities3)                      

#2       cities.intersection_update(cities2)        # This updates in the existing sets
#       print(cities)
    #   order is not valid for all in the sets
    #1 and 2  are intersection sections that prints or returns only the same elements

# cities3=cities.symmetric_difference(cities2)        # This returns a new set  
# print(cities3)


# cities3=cities.symmetric_difference_update(cities2)        # This updates in the existing sets 
# print(cities3)

# cities3=cities.difference(cities2)
# print(cities3)

print(cities.issuperset(cities4))
print(cities4.issuperset(cities))
print(cities4.issubset(cities))
print(cities.issubset(cities4))

cities.add("Newyork")
print(cities)
cities.remove("Tokyo")      #remove() or discard()          discard doesn't throws any error
print(cities)

cities.pop()
print(cities)



# del delets the entire set
#clear() delets only the elements inside the set
#