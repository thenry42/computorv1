from parser import Term


def get_roots(terms: list[Term], delta: float):
    if (delta == 0): # 1 possible solution
        return get_only_root(terms)
    elif (delta > 1): # 2 roots
        return get_two_roots(terms)
    else:
        return get_complex_roots(terms)


def get_only_root(terms: list[Term]):
    return 0


def get_two_roots(terms: list[Term]):
    return 0


def get_complex_roots(terms: list[Term]):
    return 0