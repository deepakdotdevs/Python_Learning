# recursion is a process in which a function calls itself till a certain condition is not met is called recursion
# eg; Factorial of n => n*(n-1)*(n-2)*...2*1
# n!
# 4! = 4*3*2*1 = 24

# Without recursion :
# def fact(num):
#     factorial =1
#     while num>1:
#         factorial *=num
#         num-=1
#     return factorial
# num=5
# print(f"Factorial of {num} is {fact(num)}")

# With recursion :
# There are 2 parts to any recursive function
# 1. Base/terminal condition
# 2. Recursive condition
# def fact(num):
#     if num==1:
#         return 1
#     else:
#         factorial = num*fact(num-1)
#         return factorial
# print(fact(5))