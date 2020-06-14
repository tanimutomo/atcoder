n = int(input())
a = list(map(int, input().split()))

a = sorted(a)

ps = [a[0]]
dup = []
for ai in a[1:]:
    is_divided = False
    for p in ps:
        if ai % p == 0:
            if ai == p and ai not in dup:
                dup.append(ai)
            is_divided = True
            break

    if not is_divided:
        ps.append(ai)

print(len(ps) - len(dup))