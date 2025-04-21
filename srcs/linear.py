from Term import Term
from delta import get_letter

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