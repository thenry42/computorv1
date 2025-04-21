import sys
from parser import parse_input
from reduced import get_reduced, get_polynomial_degree
from delta import get_delta
from roots import get_roots
from linear import get_linear_solution
from tests import launch_tests
from Term import Term

# The Every term in the equation will be in the following format:
# a * X^p
class Term:
    def __init__(self, coefficient: float, power: int, sign: int):
        self.coefficient = coefficient
        self.power = power
        self.sign = sign


def main():

    solutions = []
    degree = -1
    terms = []

    try:
        # 1. Parse the input OR launch tests
        if len(sys.argv) != 2:
            print("Usage: ./computor <equation>")
            return 1
        if len(sys.argv) == 2 and sys.argv[1] == "--test":
            launch_tests()
            return 1
        terms = parse_input(sys.argv[1])

        # 2. Get reduced form of the equation (a * X^2 + b * X + c = 0)
        degree = get_polynomial_degree(terms)
        terms = get_reduced(terms)

        # 3. Given the degree of the equation, we choose the solving method
        if degree == 0:
            # if a - b == 0 => all real nb are solution
            # elif a - b != 0 => no solution
            pass
        elif degree == 1:
            # 3.a. calculate Linear solution (if not quadratic)
            solutions = get_linear_solution(terms)
        elif degree == 2:
            # 3.b. calculate the discriminant (delta) if quadratic
            delta = get_delta(terms)
            # 4. calculate the solutions
            solutions = get_roots(terms, delta)
        else:
            print("Polynomial degree:", degree)
            print("The polynomial degree is strictly greater than 2, I can't solve.")
            return 1

        # 5. Displays solution in a nice fashion
        if isinstance(solutions, list):
            formatted_solutions = [f"{sol:.6f}" for sol in solutions]
            print(formatted_solutions)
        else:
            print(f"{solutions:.6f}")
    
    except Exception as e:
        print(f"Error: {e}")

    return 0

if __name__ == "__main__":
    main()
