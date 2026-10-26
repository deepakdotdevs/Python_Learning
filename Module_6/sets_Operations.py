nums={1,3,2,0,-1}
nums_2={}
# membership operator : in & not in
print(0 in nums)
print(10 in nums)
print(0 not in nums)
print(10 not in nums)

# slicing & indexing is not possible in sets

# concatenation in sets ("+" operator is not supported as list & tuple for concatenation in sets)

# repeation sets : ("*" operator is not supported too for repeation)

print("-------------------------")

weekdays = ('Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun')
print(weekdays, type(weekdays))
# convert this tuple into a set using typecasting
weekdays = set(weekdays)
print(weekdays, type(weekdays))

# Are sets mutable or immutable?
# --> Sets are mutable

set1 = {2,0,-1}
# set1[0] = 10 # we can't do this way, as it not have indexing

# add() : add elements to the set
set1.add(5)
print(set1)

# remove() 
set1.remove(0)
print(set1)
# set1.remove(10) # keyerror through

set1.add(5) # add something which is already present does't gives any error
print(set1)

# discard() :
set1.discard(2)
print(set1)

set1.discard(20)
print(set1)

# diff b/w remove() & discard() is remove gives error if we delete something which is not already in sets, whereas discard() not gives any error for same.