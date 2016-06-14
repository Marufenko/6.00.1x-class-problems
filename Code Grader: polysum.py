import math

def polysum(n,s):
    '''
    This function should sum the area and square of the perimeter of the regular polygon. 
    '''
    area = abs((0.25*n*s**2)/(math.tan(math.pi/n)))
    square = (n * s)**2
    sum = area + square
    return round(sum,4)
