from term import Term
from utils import get_letter


def my_sqrt(x: float):
    """ Calculate the square root of a number """
    return (x ** 0.5)    

def get_roots(terms: list[Term], delta: float):

    x = [] 
    b = get_letter(terms, 'b')
    a = get_letter(terms, 'a')
    c = get_letter(terms, 'c')
    
    if (delta == 0): # 1 possible solution
        x = -b / (2 * a)
    elif (delta > 1): # 2 roots
        tmp = (-b - (my_sqrt(delta))) / (2 * a) 
        x.append(tmp)
        tmp = (-b + (my_sqrt(delta))) / (2 * a)
        x.append(tmp)
    elif (delta < 0): # 2 complex solutions
        real = -b / (2 * a)
        imaginary = my_sqrt(-delta) / (2 * a)
        x.append(complex(real, imaginary))
        x.append(complex(real, -imaginary))
    return x
