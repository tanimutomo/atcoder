N = int(input())
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]
C = [int(i) for i in input().split()]

counter = 0
for i in range(N):
    # print(i)
    num = A[i] - 1
    counter += B[num]
    # print('Add:', B[num])
    if i != 0 and num - 1 == A[i-1] - 1:
        counter += C[num-1]
        # print('Add:', C[num-1])
    # print('')
print(counter)
