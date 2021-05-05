#1
def a():
    return 5
print(a())
# Prediction: prints 5
# Correct! 

#2
def a():
    return 5
print(a()+a())
# Prediction: prints 10
# Correct! 

#3
def a():
    return 5
    return 10
print(a())
# Prediction: prints 5
# Correct! 

#4
def a():
    return 5
    print(10)
print(a())
# Prediction: returns 5, prints 5
# Correct! 

#5
def a():
    print(5)
x = a()
print(x)
# Prediction: prints 5, returns None, prints None
# Correct! 

#6
def a(b,c):
    print(b+c)
#print(a(1,2) + a(2,3))
# Prediction: prints 3, 5, None
# Wrong! Error is thrown when line 42 attempts to add (None + None)

#7
def a(b,c):
    return str(b)+str(c)
print(a(2,5))
# Prediction: prints 25
# Correct! 

#8
def a():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(a())
# Prediction: prints 100, 10
# Correct! 

#9
def a(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(a(2,3))
print(a(5,3))
print(a(2,3) + a(5,3))
# Prediction: prints 7, 14, 21
# Correct! 

#10
def a(b,c):
    return b+c
    return 10
print(a(3,5))
# Prediction: prints 8
# Correct! 

#11
b = 500
print(b)
def a():
    b = 300
    print(b)
print(b)
a()
print(b)
# Prediction: prints 500, 500, 300, 500
# Correct! 

#12
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
a()
print(b)
# Prediction: prints 500, 500, 300, 500
# Correct! 

#13
b = 500
print(b)
def a():
    b = 300
    print(b)
    return b
print(b)
b=a()
print(b)
# Prediction: prints 500, 500, 300, 300
# Correct! 

#14
def a():
    print(1)
    b()
    print(2)
def b():
    print(3)
a()
# Prediction: prints 1, 3, 2
# Correct! 

#15
def a():
    print(1)
    x = b()
    print(x)
    return 10
def b():
    print(3)
    return 5
y = a()
print(y)
# Prediction: prints 1, 3, 5, 10
# Correct! 