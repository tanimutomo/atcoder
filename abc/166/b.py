n, k = map(int, input().split())
d_list = list()
s = set()
for i in range(k):
    d_list.append(int(input()))
    s |= set(list(map(int, input().split())))

print(n - len(s))