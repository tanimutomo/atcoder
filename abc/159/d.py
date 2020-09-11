n = int(input())
a = list(map(int, input().split()))
s = list(set(a))
d = {str(si): 0 for si in s}

for ai in a:
    d[str(ai)] += 1

cd = dict()
for k, v in d.items():
    cd[k] = v*(v-1)//2

sm = sum(list(cd.values()))

for ai in a:
    di = d[str(ai)]
    print(sm - cd[str(ai)] + (di-1)*(di-2)//2)