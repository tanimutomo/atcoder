def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

n = int(input())
a = list(map(int, input().split()))

a = sorted(a)
ads = [0]*(2*10**5)

ans = 0
dups = []
for ai in a:
    ds = make_divisors(ai)
    ok = True
    if ads[ai]:
        if ai not in dups:
            dups.append(ai)
        continue
    for d in ds:
        if ads[d]:
            ok = False
            break
    if ok:
        ads[ai] = 1
        ans += 1

print(ans - len(dups))