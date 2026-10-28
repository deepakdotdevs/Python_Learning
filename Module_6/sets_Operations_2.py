# Operations on sets - union, interaction & difference

# st1={"English", 'Maths', 'CS', 'Chemistry', 'Physics'}
# st2={"English", 'Bio', 'Chemistry', 'Physics'}
# st3={"Sanskrit", 'CS','Grammer'}
# print(st1, type(st1))
# print(st2, type(st2))

# # How to find out the common subjects between student 1 and student 2 : 
# # Means for intersection : 
# common_subjects = st1.intersection(st2,st3)
# common_subjects = st1 & st2 # also we use "&" as interaction operator
# print(common_subjects)
# # When no common, it returns empty set - set()

# # Union of sets : 
# # all_subjects = st1.union(st2, st3)
# all_subjects = st1 | st2 | st3 # | this is dot union operator use for union of the set
# print(all_subjects)
# # Concatenation in sets, means joining as known as union of sets too

# Difference b/w sets :
days = {'Mon', 'Tue', 'Wed', 'Thu', 'Fri', "Sat", 'Sun'}
weekends = {'Sat', 'Sun'}
weekends = days-weekends # elements of days which are not in weekends
# weekends = days.difference(weekends)
print(weekends)
# difference can apply using minus "-" operator or difference function