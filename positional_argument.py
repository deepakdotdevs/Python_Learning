# # Variable length positional arguments : 
# # *args - means star number of arguments 
# # *args - variable length positional arguments (0 to n)
# def add(*args):
#     print(args, type(args))
#     return sum(args) # sum() for the total calculation 
# res=add(1,2,3,4,5,6,7,8,9)
# print(res)
# # what there values are getting stored as? (*args) ?? - Tuple data type is this
# # In *args 'args' is not mandantory we use any variable name but with *

# # *args exhaust all the positional arguments

# Example No. 2 - of *args : 
def students_details(sid, name, *marks):
    if len(marks) ==0:
        print(f"{name} with id {sid} was absent..!!")
    else:
        percent=sum(marks)/len(marks)
        print(f"{name} with id {sid} secured {percent}%")
students_details(101, 'Deepak', 87, 69, 81, 74.2)
students_details(102, 'Thakurr', 91.0, 49.5, 84.0, 74.3, 86.45)
students_details(103, 'Sahdev', 65,4, 74, 89.2)
students_details(104, 'Har')
