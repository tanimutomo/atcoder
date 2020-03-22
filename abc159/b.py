s = input()

n = len(s)
s_h = s[:(n-1)//2]
s_f = s[(n+2)//2:]

if s == s[::-1] and s_h == s_h[::-1] and s_f == s_f[::-1]:
    print('Yes')
else:
    print('No')