from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    a, b = tup()
    c, d = tup()

    dis = abs(a - c) + abs(b - d)

    if dis == 0:
        print(0)
    elif dis <= 3:
        print(1)
    elif (a + b == c + d) or (a - b == c - d):
        print(1)
    elif dis % 2 == 0:
        print(2)
    elif abs((a + b) - (c + d)) <= 3:
        print(2)
    elif abs((a - b) - (c - d)) <= 3:
        print(2)
    else:
        print(3)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
