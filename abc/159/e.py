import numpy as np
import pprint
import sys

h, w, k = list(map(int, input().split()))
c_org = np.array([list(map(int, list(input()))) for _ in range(h)])
if c_org.sum() <= k:
    print(0)
    sys.exit()

cs = [c_org]

def wsearch(cs, cnt :int, is_sat :bool):
    if is_sat:
        print(cnt)
        sys.exit()
    cnt += 1
    for c in cs:
        h, w = c.shape
        for hi in range(1, h):
            c_new = [c[hi:, :], c[:hi, :]]
            is_sat = True
            for i, c in enumerate(cs):
                if c.sum() > k:
                    is_sat = False
                    break
            if is_sat:
                return wsearch(c_new, cnt, True)
            else:
                return wsearch(c_new, cnt, False)

        for wi in range(1, w):
            c_new = [c[:, wi:], c[:, :wi]]
            is_sat = True
            for i, c in enumerate(cs):
                if c.sum() > k:
                    is_sat = False
                    break
            if is_sat:
                return wsearch(c_new, cnt, True)
            else:
                return wsearch(c_new, cnt, False)

wsearch(cs, 0, False)