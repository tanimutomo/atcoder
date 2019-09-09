N = int(input())
B = [int(i) for i in input().split()]

A_sum = 0
for i in range(N):
    if i == 0:
        A_sum += B[i]
    elif i == N-1:
        A_sum += B[i-1]
    else:
        A_sum += min(B[i], B[i-1])
print(A_sum)
