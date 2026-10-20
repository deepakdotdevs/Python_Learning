# Type Casting - Boolean

val1 = True
print(val1)
print(type(val1))

# let's try to convert this into string
val1=str(val1)
print(type(val1))
print(val1)

# string into boolean : 
val2 = "Python"
print(type(val2))
val2 = bool(val2)
print(type(val2))
print(val2)

# integer & float into boolean : 
val3 = 100
print(type(val3))
val3 = bool(val3)
print(type(val3))

val4 = 42.03
print(type(val4))
val4 = bool(val4)
print(type(val4))

val5 = 0
print(type(val5))
print(val5)
val5 = bool(val5)
print(type(val5))
print(val5)

# When 0 gives False
# When Positive or Negative integer gives True
# When Float gives True, but 0.0 gives False

# Strings : 
# Note - Except empty strings, everything will gives True

str1 = ""
str2 = ''
str3 = ''''''
str1 = bool(str1)
str2 = bool(str2)
str3 = bool(str3)
print(type(str1))
print(type(str2))
print(type(str3))
print(str1)
print(str2)
print(str3)

# None into Boolean : Always return False

val10 = None
print(type(val10))
val10 = bool(val10)
print(val10)
print(type(val10))
print("\n")

print("------------------------\n")

val0 = True
print(val0)
print(type(val0))
val0 = int(val0)
print(val0)
print(type(val0))

val0 = False
print(val0)
print(type(val0))
val0 = int(val0)
print(val0)
print(type(val0))

val0 = True
print(val0)
print(type(val0))
val0 = float(val0)
print(val0)
print(type(val0))

val0 = False
print(val0)
print(type(val0))
val0 = float(val0)
print(val0)
print(type(val0))