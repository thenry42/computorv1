import sys
from parser import parse_input


def main():

    # 1. Parse the input
    if len(sys.argv) != 2:
        print("Usage: ./computor <equation>")
        return 1

    equation_str = parse_input(sys.argv[1])
    print(equation_str)
    
    # 2. get reduced form

    # 3. calculate the discriminant (delta)

    # 4. calculate the roots

    # 5. print the results


    return 0

if __name__ == "__main__":
    main()
