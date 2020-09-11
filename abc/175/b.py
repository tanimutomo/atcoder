n = int(input())
ls = list(map(int, input().split()))
ls = sorted(ls)

cnt = 0

for i in range(n):
    li = ls[i]
    for j in range(i+1, n):
        lj = ls[j]
        if li == lj:
            continue
        for k in range(j+1, n):
            lk = ls[k]
            if lj == lk:
                continue
            if li + lj <= lk:
                break
            cnt += 1

print(cnt)