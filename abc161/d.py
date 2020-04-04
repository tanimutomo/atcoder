import sys

k = int(input())

rs = [i for i in range(1, 10)]
if k <= 9:
    print(rs[k])
    sys.exit()

def is_rnrn(x):
    x = list(map(int, list(str(x))))
    for i in range(len(x)-1):
        if abs(x[i] - x[i+1]) > 1:
            return False
    return True

def get_next(x):
    x_new = x + 9
    if is_rnrn(x_new):
        return x_new
    else:
        if str(x) == '9'*len(str(x)):
            return x+1
        if is_rnrn((x // 100 + 1) * 100):
            return (x // 100 + 1) * 100
        x_3 = str(x)[-3]
        x_new = [int(x_3)+1 - i for i in range(3)]
        return int(str(x)[:-3] + ''.join(list(map(str, x_new))))


cnt, gcnt = 9, 0
lev = 2
i, i_ = 10, -1
while True:
    print(cnt, ':', i, is_rnrn(i))
    if i == i_: break
    i_ = i
    if is_rnrn(i):
        cnt += 1
        if cnt == k:
            print(i)
            sys.exit()
        i += 1
    else:
        i = get_next(i-1)
    gcnt += 1