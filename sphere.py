"""
Jackson Calvert
Prof Cafiero
sphere.py
CS1210 C
"""

import math

def surface_area(x):
    p = (4 * math.pi) * (x ** 2)
    return f"{p: .02f}"

def volume(y):
    d = ((4/3) * math.pi) * (y ** 3)
    return f"{d: .02f}"

radius = int(input("What is the radius of the circle? "))
print(f"The Suraface Area of this circle is {surface_area(radius)}.")
print(f"The Volume of this circle is {volume(radius)}.")