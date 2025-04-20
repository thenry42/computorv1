from parser import Term


def get_roots(terms: list[Term], delta: float):
    if (delta == 0): # 1 possible solution
        return get_only_root(terms)
    elif (delta > 1): # 2 roots
        return get_two_roots(terms)
    else:
        return get_complex_roots(terms)


def get_only_root(terms: list[Term]):
    # x = -b / 2a

    return 0


def get_two_roots(terms: list[Term]):
    # x1 = (-b-sqrt(delta)) / 2a
    # x2 = (-b+sqrt(delta)) / 2a
    
    return 0


def get_complex_roots(terms: list[Term]):
    # complex roots can be found using the formulas above
    # BUT it requires to use i (imginary numbers)
    # i = sqrt(-1) <=> i^2 = -1
    return 0