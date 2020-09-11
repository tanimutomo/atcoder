s = input()

cnt = 0
mx = 0

for si in s:
    if si == "R":
        cnt += 1
    else:
        cnt = 0
    if mx < cnt:
        mx = cnt

print(mx)