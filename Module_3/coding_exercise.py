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

