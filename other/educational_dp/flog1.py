from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    _ = int(input())
    hs = vec()
    hs.reverse()

    cs = [0 for _ in range(len(hs))]
    cs[0] = 0
    cs[1] = abs(hs[0] - hs[1])

    i = 2
    while True:
        if i == len(hs): break
        one = cs[i-1] + abs(hs[i-1] - hs[i])
        two = cs[i-2] + abs(hs[i-2] - hs[i])
        cs[i] = two if two <= one else one
        i += 1

    print(cs[-1])


# Recursion Version (cannot use because of recurtion limitation)
# def minpath(now):
#     if now == len(hs)-1: return 0
#     if now == len(hs)-2: return abs(hs[now] - hs[now+1])
#     return min([
#         minpath(now+1) + abs(hs[now] - hs[now+1]),
#         minpath(now+2) + abs(hs[now] - hs[now+2]),
#     ])


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
