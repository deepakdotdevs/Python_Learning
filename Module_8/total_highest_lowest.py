# How to find minimum, maximum and sum or total of numbers or integers..!

scores = [2,45,102,4,9, 12,45,90, 1,0,1]
print(len(scores))
# Find the sum of total score of the team using for loop :
# total=0
# for i in scores:
#     total = total+i
# print(f"Total Sum is {total}")

# # sum() we use without any loop
# total = sum(scores)
# print(f"Total Score is {total}")

# Find the Highest Score : 
highest = scores[0] # assume that the first value is highest
for i in scores:
    if highest<i:
        highest = i
print(f"Highest Score is {highest}")
# max() we use for same
highest = max(scores)
print(highest)

# Find the Lowest Score : 
lowest = scores[0]
for i in scores:
    if i<lowest:
        lowest=i
print(f"Lowest Score is {lowest}")
# min() we use for same
lowest = min(scores)
print(lowest)