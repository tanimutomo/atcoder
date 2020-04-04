from collections import deque
import sys

k = int(input())

q = deque([i for i in range(1, 10)])
if k <= 9:
    print(q[k-1])
    sys.exit()

cnt = 0
while True:
    if cnt == k:
        print(x)
        break
    x = q.popleft()
    m = x % 10
    if m == 0:
        q.extend([10*x + m, 10*x + (m+1)])
    elif m == 9:
        q.extend([10*x + (m-1), 10*x + m])
    else:
        q.extend([10*x + (m-1), 10*x + m, 10*x + (m+1)])
    cnt += 1