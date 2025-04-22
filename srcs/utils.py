from term import Term


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


def get_linear_solution(terms: list[Term]):
    # x = -c / b with b != 0
    
    b = get_letter(terms, 'b')
    c = get_letter(terms, 'c')

    if b == 0:
        if c == 0:
            print("Linear equation is true for all Real numbers")
        else:
            print("No solution for this linear equation")
    else:
        x = -c / b
        return x
    
    return None


def get_reduced(terms: list[Term]):

    degree = get_polynomial_degree(terms)

    reduced_terms = []
    terms_by_power = {} # dictionary by power

    for term in terms:
        power = term.power
        coef = term.coefficient * term.sign
        if power in terms_by_power:
            terms_by_power[power] += coef
        else:
            terms_by_power[power] = coef

    for power, coef in sorted(terms_by_power.items()):
        if coef >= 0:
            sign = 1
        else:
            sign = -1
        reduced_terms.append(Term(abs(coef), power, sign))

    return reduced_terms


def get_polynomial_degree(terms: list[Term]):

    degree = 0
    for term in terms:
        if term.power >= degree:
            degree = term.power
    return degree


def get_reduced_str(terms: list[Term], degree: int):
    """
    Generate a string representation of the reduced form of the equation.
    Terms are already combined, but need to be sorted and formatted properly.
    """
    # Sort terms by power (descending)
    sorted_terms = sorted(terms, key=lambda term: term.power, reverse=True)
    
    # Build the reduced form string
    reduced_str = ""
    is_first_term = True
    
    for term in sorted_terms:
        coef = term.coefficient * term.sign
        
        # Skip terms with zero coefficient
        if abs(coef) < 1e-10:
            continue
            
        # Determine sign for output
        if is_first_term:
            if coef < 0:
                reduced_str += "-"
        else:
            if coef < 0:
                reduced_str += " - "
            else:
                reduced_str += " + "
        
        # Format the coefficient and power
        coef_abs = abs(coef)
        coef_str = f"{coef_abs:.6f}".rstrip('0').rstrip('.') if coef_abs != int(coef_abs) else str(int(coef_abs))
        
        if term.power == 0:
            reduced_str += f"{coef_str}"
        elif term.power == 1:
            reduced_str += f"{coef_str} * X"
        else:
            reduced_str += f"{coef_str} * X^{term.power}"
        
        is_first_term = False
    
    # Handle the case when all coefficients are zero
    if not reduced_str:
        reduced_str = "0"
    
    # Add the "= 0" part
    reduced_str += " = 0"
    
    return reduced_str 