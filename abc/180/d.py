from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    x, y, a, b = tup()

    n = math.floor(math.log(b/x*(a-1), a) + 1)

    if a**n * x >= y:
        print(math.floor(math.log(y/x, a)))
        return
    
    m = math.floor((y - (a**n * x)) / b)
    print(m + n)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
