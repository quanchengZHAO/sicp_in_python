import operator

""" Write procedures for addition, subtraction, and multiplication modulo n"""
def add_mod(a, b, n):
    return (a + b) % n


def subtraction_mod(a, b, n):
    return (a - b) % n


def multiplication_mod(a, b, n):
    return (a * b) % n

def modular(modulus, op):
    return lambda x, y:  op(x, y) % modulus

