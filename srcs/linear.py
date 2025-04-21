from parser import Term
from delta import get_letter

def get_linear_solution(terms: list[Term]):
    # x = -c / b with b != 0
    
    c = get_letter(terms, 'c')
    b = get_letter(terms, 'b')

    x = -c / b
    return x