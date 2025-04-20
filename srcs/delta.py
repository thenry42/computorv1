from parser import Term

# calculate the discriminant (delta) of the quadratic equation

def get_delta(terms: list[Term]):
    # delta = b^2 - 4ac

    a, b, c = 0, 0, 0
    for term in terms:
        if term.power == 0:
            c += term.coefficient * term.sign
        elif term.power == 1:
            b += term.coefficient * term.sign
        elif term.power == 2:
            a += term.coefficient * term.sign
        else:
            raise ValueError("Delta problem")
    
    delta = (b * b) - (4 * a * c)
    print("Delta: ", delta)
    return delta
    
    