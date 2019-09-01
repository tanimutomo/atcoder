N = int(input())
A = list()
for i in range(N):
    A.append([int(a) - 1 for a in input().split()])
# print(A)

days = 0
for d in range(1, 2*N):
    # print('day:', d)
    game_counter = 0
    A_avail = [True for i in range(N)]
    for i in range(N):
        if len(A[i]) == 0:
            A_avail[i] = False
    if sum(A_avail) == 0:
        print(d - 1)
        break
    for i in range(N):
        # print('player:', i)
        if not A_avail[i]:
            # print('player is not available')
            continue
        e = A[i][0]
        # print(e, 'is enemy')
        if A_avail[e] and A[e][0] == i:
            # print(i, 'vs', e)
            A[i].pop(0)
            A[e].pop(0)
            A_avail[i] = False
            A_avail[e] = False
            game_counter += 1
        # print('')
    if game_counter == 0:
        print(-1)
        break
