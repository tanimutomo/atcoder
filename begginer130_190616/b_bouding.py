N, X = [int(i) for i in input().split()]
L = [int(i) for i in input().split()]

now = 0
count = 1
for l in L:
    now += l
    if now > X:
        break
    else:
        count += 1

print(count)
