def my_sqrt(x: float):
    """
    Calculate the square root of a number using Newton's method
    
    Args:
        x: The number to calculate the square root of
        
    Returns:
        The square root of x
    """
    if x < 0:
        raise ValueError("Cannot calculate square root of a negative number")
    
    if x == 0:
        return 0
        
    # Initial guess
    guess = x / 2
    
    # Precision threshold
    epsilon = 0.0000001
    
    # Newton's method iteration
    while True:
        # Calculate a better approximation
        better_guess = (guess + x / guess) / 2
        
        # Check if we've reached sufficient precision
        if abs(better_guess - guess) < epsilon:
            return better_guess
            
        # Update guess
        guess = better_guess