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
    elif euclid_dist_1(a, b, c, d) <= math.sqrt(5):
        print(2)
    elif euclid_dist_2(a, b, c, d) <= math.sqrt(5):
        print(2)
    else:
        print(3)


def euclid_dist_1(a, b, c, d: int) -> float:
    return abs(c - d + b - a) / math.sqrt(2)


def euclid_dist_2(a, b, c, d: int) -> float:
    return abs(c + d - b - a) / math.sqrt(2)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
