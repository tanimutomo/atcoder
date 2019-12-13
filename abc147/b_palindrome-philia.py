s = str(input())

if len(s) % 2 == 0:
    fore = s[:len(s)//2]
    back = s[len(s)//2:]
else:
    fore = s[:len(s)//2]
    back = s[len(s)//2+1:]

rback = list(reversed(back))
fore = [s for s in fore]

count = 0
for rb, fo in zip(rback, fore):
    if rb != fo:
        count += 1

print(count)
