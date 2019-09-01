N = int(input())
H = [int(h) for h in input().split()]

max_num = 0
next_i = 0
for i in range(N-1):
    # print(i)
    if i != next_i:
        # print('passed')
        continue
    num = 0
    for j in range(i, N-1):
        if H[j] >= H[j+1]:
            num += 1
        else:
            break
    # print('num:', num)
    if num > max_num:
        max_num = num
        # print('max num is updated')
    next_i = i + num + 1
    # print('next_i:', next_i)
    # print('')

print(max_num)
