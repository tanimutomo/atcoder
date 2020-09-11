s = input()
Q = int(input())

qs = list()
for i in range(Q):
    qs.append(input().split())

cnt_r = 0
bs, es = '', ''
for q in qs:
    if len(q) == 1:
        cnt_r += 1
    else:
        f, c = int(q[1]), q[2]
        if f == 1:
            if cnt_r % 2 == 1:
                es += c
            else:
                bs = c + bs
        else:
            if cnt_r % 2 == 1:
                bs = c + bs
            else:
                es += c

ns = bs + s + es
if cnt_r % 2 == 1:
    print(ns[::-1])
else:
    print(ns)
