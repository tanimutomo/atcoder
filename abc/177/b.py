s = str(input())
t = str(input())

mn = 10000
for i in range(len(s)-len(t)+1):
    s_ = s[i:i+len(t)]
    ne = 0
    for j in range(len(t)):
        if s_[j] != t[j]:
            ne += 1
    if ne < mn:
        mn = ne

print(mn)