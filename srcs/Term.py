# The Every term in the equation will be in the following format:
# a * X^p
# where a is the coefficient & p is the power
class Term:
    def __init__(self, coefficient: float, power: int, sign: int):
        self.coefficient = coefficient
        self.power = power
        self.sign = sign