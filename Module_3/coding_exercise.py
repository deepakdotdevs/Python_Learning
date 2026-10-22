# Area of Triangle : 

a = float(input("Enter 1st side of triangle : "))
b = float(input("Enter 2nd side of triangle : "))
c = float(input("Enter 3rd side of triangle : "))

# s = semiperimeter
s = (a+b+c)/2
area_part_1 = s*(s-a)*(s-b)*(s-c)
full_area = area_part_1**0.5
print("Area of triangle is : ", full_area)
print("Area of triangle is : ", round(full_area, 2))

# Simple Interest : 

principal_amt = float(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest : "))
time_duration = float(input("Enter Time Duration : "))
simple_interest = (principal_amt*rate*time_duration)/100
print("Simple Interest is : ", simple_interest)

# Compound Interest : 

principal_amt = float(input("Enter Principal Amount : "))
rate = float(input("Enter Rate of Interest : "))
time_duration = float(input("Enter Time Duration : "))
# amt_1 = principal_amt*(1+(rate/100))**time_duration
amt_2 = principal_amt*pow(1+(rate/100), time_duration)
compound_Interest=amt_2-principal_amt
print(round(compound_Interest, 2))

# Area of right-angled triangle : Base & Height is given !!

base = float(input("Enter Base of Triangle : "))
height = float(input("Enter Height of Triangle : "))
area = (1/2)*(base*height)
print("Area of right-angled triangle : ", area)
