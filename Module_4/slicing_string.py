s1 = "Hello World"

# length of string
print(len(s1))

# Indexing 
print("First char", s1[0])
print("First char", s1[-1])

# Slicing is used to extract a portion of a string, list, or tuple.
# Syntax of Indexing: string[index]
# Syntax of slicing: string[start:end:step]
# start: starting index at which the slicing operation starts
# end: ending index at which the slicing stops (excluded)
# step: integer that specifies the step for the slicing

print(s1[2:7]) # llo W
print(s1[2:7:1]) # llo W
print(s1[2:7:2]) # loW
print(s1[2:9:2]) # loWr
print(s1[1:12:3]) # eood

s1_slice = s1[2:7:1]
print(type(s1_slice))
