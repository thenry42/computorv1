import sys
from parser import parse_input
from reduced import get_reduced
from delta import get_delta
from roots import get_roots


def main():

    # 1. Parse the input
    if len(sys.argv) != 2:
        print("Usage: ./computor <equation>")
        return 1

    test1 = "5 * X^0 + 4 * X^1 = 4 * X^0"
    test2 = "5 * X^0 + 4 * X^1 - 9.3 * X^2 = 1 * X^0"
    terms = parse_input(test2)

    # 2. get reduced form (a * X^2 + b * X + c = 0)

    terms = get_reduced(terms)

    # 3. calculate the discriminant (delta)

    delta = get_delta(terms)

    # 4. calculate the solutions

    solutions = get_roots(terms, delta)

    # 5. print the results

    if isinstance(solutions, list):
        formatted_solutions = [f"{sol:.6f}" for sol in solutions]
        print(formatted_solutions)
    else:
        print(f"{solutions:.6f}")

    return 0

if __name__ == "__main__":
    main()
