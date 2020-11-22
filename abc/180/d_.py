from collections import Counter, deque
from itertools import combinations
import math
import sys


def main():
    ans()


def ans():
    x,y,a,b=map(int,input().split())
 
    ans=0
    while a*x<=x+b and a*x<y:
        x*=a
        ans+=1
    
    print(ans+(y-1-x)//b)


def tup():
    return map(int, input().split())


def vec():
    return list(map(int, input().split()))


def mat(rows :int):
    return [list(map(int, input().split())) for _ in range(rows)]


if __name__ == "__main__":
    main()
