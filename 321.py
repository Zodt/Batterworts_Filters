from sympy import symbols, pi, cos, product


def products(n):
    p, k = symbols('p'), symbols('k', integer=True)
    if n % 2:
        a = str((p + 1) * product((p ** 2) - 2 * p * cos(((2 * k + n - 1) / (2 * n)) * pi) + 1, (k, 1, (n - 1) // 2)).evalf())
    else:
        a = str(product((p ** 2) - 2 * p * cos(((2 * k + n - 1) / (2 * n)) * pi) + 1, (k, 1, n // 2)).evalf())

    return a.replace('1.00000000000000', '1')


print(products(0))
print(products(1))
print(products(2))
print(products(3))
print(products(4))
print(products(5))
print(products(6))
print(products(7))
print(products(8))
print(products(9))


