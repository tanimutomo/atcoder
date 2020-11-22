from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    x, y, z = tup()
    print(expectation(x, y, z))
    

def expectation(x, y, z: int) -> int:
    if 100 in [x, y, z]: return 0
    s = x + y + z
    return x/s * (expectation(x+1, y, z) + 1) \
         + y/s * (expectation(x, y+1, z) + 1) \
         + z/s * (expectation(x, y, z+1) + 1)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
