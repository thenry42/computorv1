from parser import Term
from delta import get_letter
from maths import my_sqrt
from math import sqrt # REMOVE FOR PUSH

def get_roots(terms: list[Term], delta: float):
    if (delta == 0): # 1 possible solution
        return get_only_root(terms)
    elif (delta > 1): # 2 roots
        return get_two_roots(terms, delta)
    else:
        return get_complex_roots(terms, delta)


def get_only_root(terms: list[Term]):
    # x = -b / 2a

    b = get_letter(terms, 'b')
    a = get_letter(terms, 'a')
    x = -b / (2 * a)
    return x


def get_two_roots(terms: list[Term], delta: float):
    # x1 = (-b-sqrt(delta)) / 2a
    # x2 = (-b+sqrt(delta)) / 2a

    x = []

    a = get_letter(terms, 'a')
    b = get_letter(terms, 'b')
    c = get_letter(terms, 'c')

    # Getting the sqrt of delta with my own function
    #d = my_sqrt(delta)

    # Getting the sqrt of delta using python builtin
    d = delta ** 0.5

    tmp = (-b - d) / (2 * a) 
    x.append(tmp)
    tmp = (-b + d) / (2 * a)
    x.append(tmp)
    
    return x


def get_complex_roots(terms: list[Term], delta: float):
    # complex roots can be found using the formulas above
    # BUT it requires to use i (imginary numbers)
    # i = sqrt(-1) <=> i^2 = -1

    x = []

    a = get_letter(terms, 'a')
    b = get_letter(terms, 'b')
    c = get_letter(terms, 'c')

    # get the real part and the imaginary part of the roots

    return x