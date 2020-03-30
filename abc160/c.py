k, n = map(int, input().split())
a = list(map(int, input().split()))
a_ = a + [k + a[0]]
d = [a_[i+1] -  a_[i] for i in range(n)]
print(sum(d) - max(d))