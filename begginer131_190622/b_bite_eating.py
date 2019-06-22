N, L = [int(i) for i in input().split()]

s = (N + 2*L - 1) / 2 * N
max_t = L + N - 1
if L >= 0:
    min_t = L
else:
    if max_t < 0:
        min_t = max_t
    else:
        min_t = 0

print(int(s - min_t))
