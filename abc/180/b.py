from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    n = int(input())
    x = vec()
    print(manhattan(x))
    print(euclid(x))
    print(chebishef(x))


def manhattan(x):
    x = [abs(xi) for xi in x]
    return sum(x)


def euclid(x):
    x = [xi**2 for xi in x]
    return sum(x) ** (1/2)


def chebishef(x):
    x = [abs(xi) for xi in x]
    return max(x)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
