n = int(input())
A = list(map(int, input().split()))

is_distinct = False
for i in range(n):
  for j in range(i+1, n):
    if A[i] == A[j]:
      is_distinct = True
      break

if is_distinct:
  print('NO')
else:
  print('YES')