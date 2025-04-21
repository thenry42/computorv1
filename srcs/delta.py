from Term import Term


def get_letter(terms: list[Term], letter: str):
    """ Get the value of the letter given in parameter.
        Retrieve a, b & c. """
    
    value = 0
    target_power = -1

    if letter == 'c':
        target_power = 0
    elif letter == 'b':
        target_power = 1
    elif letter == 'a':
        target_power = 2
    else:
        raise ValueError(f"Unknown letter: {letter}")
    
    for term in terms:
        if term.power == target_power:
            value = term.coefficient * term.sign
            break
    
    return value 


def get_delta(terms: list[Term]):
    """ Retrieve the discriminant of the quadratic equation.
    delta = b^2 - 4ac """

    a = get_letter(terms, 'a')
    b = get_letter(terms, 'b')
    c = get_letter(terms, 'c')

    if a == 0:
        print("The coefficient of X^2 is zero, this is not a quadratic equation.")
        return None

    delta = (b * b) - (4 * a * c)
    return delta


def zero_degree(terms: list[Term]):
    """ Handle zero degree possibility """

    c = get_letter(terms, 'c')
    if c == 0:
        return "All real numbers are solutions"
    else:
        return "No solution"