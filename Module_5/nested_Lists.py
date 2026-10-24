# Nested Lists : a list inside another list is called nested list

# l1 = [5, 1.5, 'Python', True, None, [1,2,3], 10]
# print(len(l1))
# print(l1[-2])

# # How we fetch the element of the internal list : 
# print(l1[-2][0])
# print(l1[-2][-1])

print("--------------------")

l2 = [[1,2], [3,4], [5,6, [0,1]]]
print(len(l2))
print(l2[2][2][-1])
print(l2[-1][2][1])
print(l2[-1][2][-1])