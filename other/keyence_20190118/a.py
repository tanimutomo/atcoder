import math

h = int(input())
w = int(input())
n = int(input())

l = max([h, w])
c = n / l 
print(math.ceil(c))