from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    a, b = tup()
    c, d = tup()
    print(a*d - b*c)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
