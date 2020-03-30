x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p = sorted(p)[a-x:]
q = sorted(q)[b-y:]
r = sorted(r, reverse=True)

pi = 0
qi = 0
ri = 0
while True:
    if ri > c-1: break
    if pi <= x-1 and qi <= y-1:
        if p[pi] < q[qi]:
            if p[pi] < r[ri]:
                p[pi] = r[ri]
                pi += 1
                ri += 1
            else:
                break
        else:
            if q[qi] < r[ri]:
                q[qi] = r[ri]
                qi += 1
                ri += 1
            else:
                break
    elif pi <= x-1:
        if p[pi] < r[ri]:
            p[pi] = r[ri]
            pi += 1
            ri += 1
        else:
            break
    elif qi <= y-1:
        if q[qi] < r[ri]:
            q[qi] = r[ri]
            qi += 1
            ri += 1
        else:
            break
    else:
        break

print(sum(p)+sum(q))