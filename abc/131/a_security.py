S = [int(i) for i in input()]

pre = -1
status = 1
for s in S:
    s = int(s)
    if s == pre:
        status = 0
    pre = s

if status == 1:
    print("Good")
else:
    print("Bad")
