from term import Term

""" 
    Example 1:
    8 * X^0 - 6 * X^1 + 0 * X^2 = 3 * X^0
    Term[0] = {8, 0, 1}
    Term[1] = {6, 1, -1}
    Term[2] = {0, 2, 1}
            =
    Term[3] = {3, 0, 1}

    ######################################

    Example 2:
    -5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0

    Term[0] = {5, 0, -1}
    Term[1] = {4, 1, 1}
    Term[2] = {9.3, 2, -1}
            =
    Term[3] = {1, 0, 1}
"""


def parse_input(equation_str: str) -> list[Term]:
    """
    Parse the input of the user
    """
    sides = equation_str.split('=')
    if len(sides) != 2:
        raise ValueError("Invalid equation format")

    # Check if the right side is already "0" (or "0.0", " 0 ", etc.)
    right_side_stripped = sides[1].strip()
    is_already_reduced = right_side_stripped == "0" or right_side_stripped == "0.0"
    
    # 1. Parse each sides
    all_terms = []
    left_terms = parse_each_sides(sides[0], 1)
    
    if not is_already_reduced:
        right_terms = parse_each_sides(sides[1], -1)
        all_terms.extend(right_terms)
    
    all_terms.extend(left_terms)
    return all_terms


def parse_each_sides(expression: str, side_multiplier: int):
    """
    Parse each side of the equation. The right side base multiplier is negated.
    """
    # Format the expression for easier parsing
    expression = expression.replace(" ", "")  # Remove all spaces
    expression = expression.replace("+", " +")
    expression = expression.replace("-", " -")
    expression = expression.replace("*", " *")
    expression = expression.replace("X^", "X^ ")
    #print(expression)

    tokens = expression.split()

    terms = []
    i = 0

    while i < len(tokens):
        # For the standard format "a * X^p", tokens appear in groups of 3:
        # tokens[i] = coefficient (with sign)
        # tokens[i+1] = "*X^" 
        # tokens[i+2] = power

        # Get the coefficient and determine the sign
        coef_str = tokens[i]
        coef = float(coef_str)
        
        # Determine sign based on coefficient's sign
        sign = side_multiplier
        if coef < 0:
            sign *= -1
            coef = abs(coef)
        
        # Skip "*X^" token
        i += 1
        
        # Get the power
        power = int(tokens[i+1])  # power is always the 3rd token in each group
        
        # Create term and add to list
        terms.append(Term(coef, power, sign))
        
        # Move to the next group of 3 tokens
        i += 2
    
    return terms