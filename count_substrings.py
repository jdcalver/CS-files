"""
Jackson Calvert
CS1210 C
2/27/24
"""

def substring_count(string, substring):
    tally = 0
    sub_len = len(substring)
    main_len = len(string)

    for letter in range(main_len - sub_len + 1):
        if string[letter:letter + sub_len] == substring:
            tally += 1

    return tally

if __name__ == '__main__':
    
    part = str(input("Enter a string: "))
    whole = str(input("Enter a substring: "))
    herman = substring_count(part, whole)
    print(f'{herman}')