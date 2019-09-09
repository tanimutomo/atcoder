N = int(input())
P = [int(i) for i in input().split()]
# P_dict = dict(zip([i for i in range(N)], P))

y = 0 # max
x = 0 # second max
counter = 0 # sum x
for l in range(N-1):
    for r in range(l+1, N):
        if l+1 == r: # init
            y = max(P[l], P[r])
            x = min(P[l], P[r])
        else:
            if P[r] > x and P[r] > y:
                x = y
                y = P[r]
            elif P[r] > x and P[r] < y:
                x = P[r]
        counter += x
        if x == N - 1:
            counter += x * (N - r - 1)
            break
print(counter)
