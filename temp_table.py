"""
Jackson Calvert
Prof Cafiero
temp_table
CS1210 C
"""

def f_to_c(f):
    c = (f -32) * (5/9)
    return c

fahrenheit = float(input("Enter temperature in degrees in F: "))
celsius = f_to_c(fahrenheit)

print(f'{"Fahrenheit":<10}'
      f'{"Celsius":>16}')
print(f'{fahrenheit - 10:>10,.01f}'
      f'{f_to_c(fahrenheit - 10):>16,.01f}')
print(f'{fahrenheit:>10,.01f}'
      f'{celsius:>16,.01f}')
print(f'{fahrenheit + 10:>10,.01f}'
      f'{f_to_c(fahrenheit + 10):>16,.01f}')