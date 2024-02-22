"""
Jackson Calvert
CS1210 C
2/21/2024
"""

def mean(x):
    if not x:
        return None
    
    num_value = sum(x)
    total = len(x)
    return num_value / total

if __name__ == '__main__':
    DATA = [11, 8, 19, 16, 13, 17, 6, 14, 16, 10,
        14, 7, 12, 4, 2, 5, 16, 14, 16, 18]
    elements = int(input('Enter an index from 0 to 19 (inclusive): '))
    avg = mean(DATA)
    if elements in DATA[0:-1]:
        print(f'The element at index {elements} is {DATA[elements]}.')
        print(f'The sum of elements in DATA is {sum(DATA)}.')
        print(f'The largest value in DATA is {max(DATA)}.')
        print(f'The smallest value in DATA is {min(DATA)}.')
        print(f'Data has {len(DATA)} elements.')
        print(f'The mean of elements in DATA is {avg: .2f}.')
    else:
        print("Invalid")
        