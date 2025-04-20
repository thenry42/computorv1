# get the reduced form of the quadratic equation
from parser import Term

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

    print("Reduced terms:")
    for i, term in enumerate(reduced_terms):
        print(f"Term[{i}] = {{{term.coefficient}, {term.power}, {term.sign}}}")
    
    return reduced_terms


def get_polynomial_degree(terms: list[Term]):

    degree = 0
    for term in terms:
        if term.power >= degree:
            degree = term.power
    print("Polynomial degree:", degree)
    return degree