import statistics

n = int(input())
# ab = [list(map(int, input().split())) for _ in range(n)]
a, b = list(), list()
for _ in range(n):
    a_, b_ = map(int, input().split())
    a.append(a_)
    b.append(b_)

a_med = statistics.median(a)
b_med = statistics.median(b)
if len(a) % 2 == 0:
    print(int(b_med - a_med + 2))
else:
    print(b_med - a_med + 1)