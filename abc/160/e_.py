x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p = sorted(p, reverse=True)[:x]
q = sorted(q, reverse=True)[:y]
r = sorted(r+p+q, reverse=True)[:x+y]

print(sum(r))