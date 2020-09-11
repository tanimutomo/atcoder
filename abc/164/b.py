th, ta, ah, aa = map(int, input().split())

while True:
    ah -= ta
    if ah <= 0:
        print("Yes")
        break
    th -= aa
    if th <= 0:
        print("No")
        break