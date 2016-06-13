def fourthPower(x):
    '''
    function that takes in one number and returns that value raised to the fourth power. 
    x: int or float.
    '''
    result = square(square(x))
    return result
