s = input()
base = 2019

cnt = 0
for i in range(len(s)-3):
    for j in range(i+4, len(s)+1):
        if int(s[i:j]) % base == 0:
            cnt += 1
print(cnt)