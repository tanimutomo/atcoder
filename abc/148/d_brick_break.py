n = int(input())
A = [int(a) for a in input().split()]

is_over = False
count = 0
for i in range(1, n+1):
    # print('i:', i)
    while True:
        # print('    A:', A)
        # print('    count:', count)
        if len(A) == 0:
            is_over = True
            break
        if A[0] == i:
            A = A[1:]
            break
        else:
            A.pop(0)
            count += 1
    if is_over:
        break

if n == count:
    print(-1)
else:
    print(count)


