n = int(input())
s = input()

colors = ['R', 'B', 'G']

cnt = 1
for c in colors:
    cnt *= s.count(c)

for i in range(n):
    w = 1
    while True:
        if i + 2*w >= n: break
        if s[i] != s[i+w] and s[i+w] != s[i+2*w] and s[i+2*w] != s[i]:
            cnt -= 1
        w += 1
print(cnt)