"""Exact checks for the schematic and elementary inequalities."""
from fractions import Fraction
from itertools import product

x = Fraction(9, 10)
cubic_taylor = 1 + x + x**2 / 2 + x**3 / 6
assert cubic_taylor > Fraction(190, 81)
assert Fraction(19, 20) - Fraction(9, 10) == Fraction(1, 20)

for width in range(1, 10):
    words = tuple(product((0, 1), repeat=width))
    for first, second in zip(words, words[1:]):
        k = next(index for index in range(width) if first[index] != second[index])
        assert first[k] == 0 and second[k] == 1
        assert all(first[k + 1:]) and not any(second[k + 1:])

for q in range(8, 1025):
    m = q.bit_length() - 1
    assert 8 * 2 ** (m - 2) >= q

print("OK: rational tail constants, 1–9 bit adjacency and finite count examples")
