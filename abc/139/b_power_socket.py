A, B = [int(i) for i in input().split()]

taps = 1
num = 0
while True:
    if taps >= B:
        break
    taps -= 1
    taps += A
    num += 1
print(num)
