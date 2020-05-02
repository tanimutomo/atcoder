k = int(input())
a, b = map(int, input().split())

is_ok = False
for i in range(a, b+1):
    if i % k == 0:
        is_ok = True
        break

if is_ok:
    print("OK")
else:
    print("NG")