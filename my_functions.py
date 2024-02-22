"""
Jackson Calvert
Professor Cafiero
CS-1210 C
"""
def sqrt(x):
    return x ** (1/2)

print (sqrt(1))
print (sqrt(5))
print (sqrt(25))
print (sqrt(2))

def hypotenuse(a, b):
    c = (a ** 2) + (b ** 2)
    return sqrt(c)

print (hypotenuse(1, 1))
print (hypotenuse(1, 2))
print (hypotenuse(3, 4))
print (hypotenuse(36, 77))

def deg_reduce(x):
    r = x % 360
    return r

print (deg_reduce(734))