# Operations on dict - updating and deleting :

# student1 = {'maths':80.5,'eng':76.0, 'phy':89.0}
# print(student1)

# # To fetch the marks of physics : two methods
# # Method I :
# print(student1['phy'])
# # print(student1['chem']) # chemistry is not in dict and it will cause an error in output
# # Method II : Use get() same work as above
# print(student1.get('phy'))
# print(student1.get('chem')) # Output is None, chem is not in dict, but error is not the output

# # If something is not present in dict, and we want to return default value differ from "None" output : 
# print(student1.get('chem', 40.0)) # Now it returns 40.0 instead of None output

# print("-------------------")
emp1={'id':1001, 'name':'John', 'salary':10000}
# print(emp1.get('phone', 9518874185))


print("---------------------")
# Membership Operator : in & not in
print(1001 in emp1) # False output, coz as value it stored
print('name' in emp1) # means it looks for the key not value

# add key-value pair, means added into a dict : 
emp1['City Pincode'] = 122107
print(emp1)

print("-------------------")

sem1_marks = {'maths':78.5, 'eng':71.0, 'phy':86.5}
sem2_marks = {'chem':81.5, 'bio':90.5}
# combine these two marks together or you want to update the marks with sem2 marks : 
# there we use update() function 
sem1_marks.update(sem2_marks)
print(sem1_marks)

groceries_1 = {'milk':60, 'rice':100, 'biscuits':20}
groceries_2 = {'rice':110, 'bread':30}
groceries_1.update(groceries_2)
print(groceries_1)

# For deletion from dictionary, function is pop() function : 
groceries_1.pop('milk')
print(groceries_1)

# keys can't be duplicat

# it reads from left to right, so output is most recent value as shown in this example :
groceries_1 = {'milk':60, 'rice':100, 'biscuits':20, 'milk':50}
print(groceries_1)
