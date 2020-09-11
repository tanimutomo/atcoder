from itertools import combinations


def combs(n, k :int) -> list:
    return list(combinations(range(1, n), k))