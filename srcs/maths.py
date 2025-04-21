def my_sqrt(x: float):
    """ Calculate the square root of a number using Newton's method """
    
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    if x == 0:
        return 0
        
    guess = x / 2
    epsilon = 0.000001
    
    while True:
        better_guess = (guess + x / guess) / 2
        if abs(better_guess - guess) < epsilon:
            return better_guess
        guess = better_guess
