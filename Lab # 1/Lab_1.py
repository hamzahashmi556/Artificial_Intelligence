# IDENTITY OPERATORS IN PYTHON

# Task # 1
print("Task # 1")
x = 6
if type(x) is int:
    print("true")
else:
    print("false")

# Task # 2
print("\nTask # 2")
x = 7.2
if type(x) is not int:
    print("true")
else:
    print("false")

# MEMBERSHIP OPERATOR:
# Task # 3
print("\nTask # 3")
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9]
for item in list1:
    if item in list2:
        print("overlapping")
    else:
        print("not overlapping")

# FLOOR DIVISION & Exponent And Assign
print("\nTask # 4")
a = 9
a //= 3
print("floor divide=", a)
a **= 5
print("exponent=", a)

# BITWISE OPERATORS
a = 60
b = 13
c = 0
c = a & b
print("Line 1", c)

c = a | b #/* 12 = 0000 1100 */
print("Line 2", c)

c = a ^ b
print("Line 3", c)

c = ~a
print("Line 4", c)

c = a << 2
print("Line 5", c)

c = a >> 2
print("Line 6", c)