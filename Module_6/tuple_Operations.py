# Operations Like : Concatenation and repetition operations

student_detail = (1001, 'John')
student_detail2 = (78.5, 91.0, 83.5, 79.5)

# Combine these two tuples into a single tuple (Use "+" operations for this operation)
student = student_detail+student_detail2
print(student)

# Repetition operation : (Use "*" operator for this)
t1 = ("Class 5", 5000)
print(t1*3)

# Membership Operations : not & not in
student_detail = (1001, 'John')
student_detail2 = (78.5, 91.0, 83.5, 79.5)
print(91.0 in student_detail2)
print(99.0 in student_detail2)
# not in 
print(91.0 not in student_detail2)
print(99.0 not in student_detail2)

# count() : 
t2 = (0,1,2,3,0,2,5,4,6,4,0,0,1,7,8)
print(t2.count(0))
print(t2.count(1))
print(t2.count(2))

# index() : returns the index of element or item in tuple
print(t2.index(2))
print(t2.index(0))
print(t2.index(40)) # as not exists through error