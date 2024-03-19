"""
Jackson Calvert
CS1210 C
2/27/24
"""

def mean(x):
    total = sum(x)
    avg = total / len(x)
    return avg

def std_dev(lst):
    avg = mean(lst)
    srq_dif = [(y - avg) ** 2 for y in lst]
    variance = sum(srq_dif) / len(lst)
    standard_deviation = variance **.5
    return standard_deviation

if __name__ == '__main__':
    lst_ = []
    
    prompt = 'Enter a real number or q to end data entry: '
    
    while True:
        element_ = float(input(prompt))
        if element_ == 'q':
            break
        lst_.append(float(element_))
            
    if element_ == 'q' and len(lst_) <= 0:
        print('No data!')
    else:
        mean_ = mean(lst_)
        std_dev_ = std_dev(lst_)
        print(f'The mean is {mean_: .2f} and the standard '
              f'deviation is {std_dev_: .2f}.')
        
    
    
       
        
        