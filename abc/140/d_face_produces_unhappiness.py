N, K = [int(i) for i in input().split()]
S = list(input())

init_score = 0
pre_s = 0
for s in S:
    if pre_s == s:
        init_score += 1
    pre_s = s

print(min(init_score + 2 * K, N - 1))
