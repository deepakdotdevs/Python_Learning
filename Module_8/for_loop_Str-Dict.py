# For loop in strings : 
# s1 = "Hello World"
# for char in s1:
#     print(char)
# print("End of the Loop")

# For loop in tuples :
# t1 = (10,20,30,40,50,60,70,80,90,100)
# for p in t1:
#     print(p)

# For loop in dictionaries :
employee = {'emp id':1001, 'name':'John', 'department':"HR"}
for i in employee:
    # print(i) # it prints only key
    # print(employee[i]) # it prints only value
    print(i, employee[i]) # it prints both

# print(employee.items())
for i in employee.items(): # it prints the entire tuple with key-value pair
    print(i) # prints key-value pair with tuple
    print(i[0]) # prints only key
    print(i[0], i[1]) # it prints key-value pair without tuple