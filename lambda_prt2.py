# filter() & map() with lambda :

# filter(): -> In list or in a tuple
# filter() in python takes a function as the argument and sequence as the second argument.
# The filter() function is used to filter elements from an iterable (list, tuple, etc.) based on a condition.
# filter() filters out the elements from the sequence for which this function returns the true.
# filter(function, sequence)

seq = [1,2,3,4]
# We want to filter out the odd numbers from the list, we want to keep the odd numbers and remove all the even nos.
# odd = lambda x: True if x%2 != 0 else False -> Use this in filtered output variable on the place of odd function in filter()
filtered_output = filter(lambda x: True if x%2 != 0 else False,seq)
print(filtered_output)
print(f"Odd nos in the above sequence are: {list(filtered_output)}")

# map() : also takes a function as the first argument and a sequence as a second argument.
# can also write lambda instead of writing a function separately and putting it here
seq = [1,2,3,4]
# lambda x: True if x%2 != 0 else False # -> Use this in filtered output variable on the place of odd function in filter()
mapped_output = map(lambda x: x ** 2,seq)
print(mapped_output)
print(f"Map Output: {list(mapped_output)}")

