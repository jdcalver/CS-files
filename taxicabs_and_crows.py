"""
Jackson Calvert
Prof Cafiero
taxicabs_and_crows.py
CS1210 C
"""

import math

STREETS_TO_MILES = 20
AVENUES_TO_MILES = 7

def taxicab_distance(x, y):
    d = (x / STREETS_TO_MILES) + (y / AVENUES_TO_MILES)
    return d

def crow_distance(x, y):
    a = math.sqrt((x / STREETS_TO_MILES) ** 2 + (y / AVENUES_TO_MILES) **2)
    return a 

streets = float(input("How many street blocks must you travel? "))
avenues = float(input("How many avenue blocks must you travel? "))
t_dist = taxicab_distance(streets, avenues)
c_dist = crow_distance(streets, avenues)
tot_dist = t_dist - c_dist

print (f"The crow\'s flight is {tot_dist: .02f} miles shorter.")