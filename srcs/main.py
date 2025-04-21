import sys
from parser import parse_input
from reduced import get_reduced, get_polynomial_degree, get_reduced_str
from delta import get_delta, zero_degree
from roots import get_roots
from linear import get_linear_solution
from Term import Term
from display import display_reduced_form, display_polynomial_degree, display_solution, display_str, display_discriminant


def main():

    solutions = []
    degree = -1
    terms = []

    try:
        # 1. Parse the input
        if len(sys.argv) != 2:
            display_str("Usage: ./computor <equation>")
            return 1
        terms = parse_input(sys.argv[1])

        # 2. Get reduced form of the equation (a * X^2 + b * X + c = 0)
        degree = get_polynomial_degree(terms)
        terms = get_reduced(terms)
        reduced_str = get_reduced_str(terms)
        
        # Display reduced form and degree
        display_reduced_form(reduced_str)
        display_polynomial_degree(degree)

        # 3. Given the degree of the equation, we choose the solving method
        if degree == 0:
            solutions = zero_degree(terms)
        elif degree == 1:
            solutions = get_linear_solution(terms)
        elif degree == 2:
            delta = get_delta(terms)
            display_discriminant(delta)
            solutions = get_roots(terms, delta)
        else:
            display_str("The polynomial degree is strictly greater than 2, I can't solve.")
            return 1

        # 4. Displays solution in a nice fashion
        display_solution(solutions)
    
    except Exception as e:
        display_str(f"Error: {e}")

    return 0

if __name__ == "__main__":
    main()
