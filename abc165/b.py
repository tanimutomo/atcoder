x = int(input())
m = 100

y = 0
while True:
    if m >= x:
        break
    y += 1
    m += int(0.01*m)
print(y)