# nested if means - if condition in if :

marks = int(input("Enter Your Marks : "))
if marks>=60:
    print("Student is Pass")
    if marks>=90:
        print("Grade A")
    elif marks>=80 and marks<90:
        print("Grade B")
    elif marks>=70 and marks<80:
        print("Grade C")
    else:
        print("Grade D")
else:
    print("Student is Fail")
