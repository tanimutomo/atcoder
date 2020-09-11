x, y = map(int, input().split())

is_exist = False
for a in range(51):
    for b in range(26):
        if a + b == x and a*2 + b*4 == y:
            is_exist = True
            break

if is_exist:
    print("Yes")
else:
    print("No")
