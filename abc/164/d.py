import re

s = input()
base = 2019

cnt = 0
i = 1
while True:
    if base * i > int(s):
        break
    idx = 0
    while True:
        idx = s.find(str(base*i), idx)
        if idx == -1:
            break
        cnt += 1
        idx += 1
    i += 1
print(cnt)