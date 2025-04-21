from Term import Term

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


def get_reduced_str(terms: list[Term]):
    reduced_str = ""
    return reduced_str 