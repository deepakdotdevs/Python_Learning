# A loop is used to execute a block of code repeatedly until a condition is met or the sequence ends.

# Two types of loop - for loop & while loop

# For Loop : 

# for loop : it is an iterator based loop which steps through the item of a collection
# (lists, tuples, sets, dict, str) and executed a block of code repeatedly
# for a number of times equal to the items/elements of that collection.print
# SYntax of for loop :-
# for var in sequence:
#     statement1
#     statement2
#     ...
#     statementN

percents = [85.5, 81.0, 86.0, 83.5] # data type is a list
# without using loop :
print(percents[0])
print(percents[1])
print(percents[2])
print(percents[3])
# with loop :
for i in percents:
    print(f"{i}")