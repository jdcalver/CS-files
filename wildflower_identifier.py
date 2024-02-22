"""
Jackson Calvert
CS1210 C
"""
import math

if __name__ == '__main__':
    
    
    petal_number = str(input(f'Does it have five petals or'
                             f' numerous thin petals? f or n: '))
    if petal_number.lower() == 'f':
        pimp_sorrel = input(f'Are the petals red '
                           f'or yellow? r or y: ')
        if pimp_sorrel.lower() == 'r':
            print("I think its a scarlet pimpernel")
        elif pimp_sorrel.lower() == 'y':
            print("I think its a wood sorrel")
        else:
            print("Invalid choice for color!")
    elif petal_number.lower() == 'n':
        dand_lawn = input(f'Are the petals yellow or '
                             f'white? y or w: ')
        if dand_lawn.lower() == 'y':
            print("I think its a common dandelion")
        elif dand_lawn.lower() == 'w':
            print("I think its a lawn daisy")
        else:
            print("Invalid choice for color!")
    else:
        print("Invalid choice for petals!")






