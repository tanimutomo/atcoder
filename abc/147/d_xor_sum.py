N = int(input())
A = [int(i) for i in input().split()]

# level_count = dict()
# for a in A:
#     bin_a = bin(a)
#     for i in range(len(bin_a[2:])):
#         if int(bin_a[-i-1]) == 1:
#             try:
#                 level_count[i] += 1
#             except:
#                 level_count[i] = 1
# 
# sum_ = 0
# for level, count in level_count.items():
#     sum_ += 2**level * count * (N - count)
# print(sum_ % (10**9 + 7))

import numpy as np

A = np.array(A)
sum_ = 0
for i in range(len(bin(np.max(A))) - 2):
    count = np.count_nonzero(A & 1)
    sum_ += 2**i * count * (N - count)
    A >>= 1
print(sum_ % (10**9 + 7))
