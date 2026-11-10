countries =['India', 'United States','Australia', 'Ireland','Sri Lanka','Iceland','Cuba','Iran','Poland']
# Count all the countries which are starting with "I"
# Method 1 :
# count =0
# for i in countries:
#     if i[0]=='I':
#         count+=1
# print(count)

# Method 2 :
# count =0
# for i in countries:
#     if i.startswith("I"):
#         count+=1
# print(count)

# Update Question with - also print all these countries as a list
count =0
output=[]
for i in countries:
    if i.startswith("I"):
        count+=1
        output.append(i)
print(count)
print(output)