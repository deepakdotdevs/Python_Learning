s1 = {1,2,4,0}
s1.add(-1)
print(s1, type(s1))
# -1 is added into the set s1, means it is mutable

# frozen sets are immutable sets
fe1 = frozenset({1,2,3,4,5})
print(fe1, type(fe1))
# fe1.add(40)
# print(fe1) # gives error as it is immutable

# Union, Intersection and difference works as usual :
fe2 = frozenset({3,4,10,20,30})
print(fe1 & fe2)
print(fe1 | fe2)
print(fe1 - fe2)
