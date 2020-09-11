n = int(input())
S, T = [str(a) for a in input().split()]

ans = ''
for s, t in zip(S, T):
    ans += s
    ans += t

print(ans)