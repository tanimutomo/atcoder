n, p = map(int, input().split())
# l = list(map(lambda x: int(x)%p, list(input())))
l = input()

cnt = 0
for i in range(n):
    for j in range(i+1, n+1):
        sm = int(l[i:j])
        if sm % p == 0:
            cnt += 1

print(cnt)