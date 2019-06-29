import sys

S = list(input())

set_s = list(set(S))
if len(set_s) != 2:
    print("No")
    sys.exit()

if S.count(set_s[0]) != 2:
    print("No")
    sys.exit()

print("Yes")
