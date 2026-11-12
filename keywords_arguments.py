# Variable length keywords arguments : 
# **kwargs - conventional to be followed not mandatory

# def func(**kwargs):
#     print(kwargs, type(kwargs))
# func(x=10, y=20)
# func() # empty dictionary
# # Data type of this or store variable in the Dictionary data type.

# Example 2 : 
def student_details(sid, sname, *extra, **marks):
    if len(marks)==0 : 
        print(f"{sname} did not attend the exam")
    else:
        percent = sum(marks.values())/len(marks)
        print(f"{sname} with id {sid} secured {percent}%")
    print(f"{sname} does {extra}")
student_details(101, 'Deepak', 'Football',sub1=78.5, sub2=81.0, sub3=90.5)
student_details(101, 'Thakur Shab', 'Tennis','basketball', sub5=78.5, sub2=81.0, sub1=90.5, sub3=82.36, sub4=72.2)