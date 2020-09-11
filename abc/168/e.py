n = int(input())
iwas = [list(map(int, input().split())) for _ in range(n)]

a_bs = dict()
m_b_as = dict()
for a, b in iwas:
    a_b =  a / b
    if a_b in a_bs.keys():
        a_bs[a_b] += 1
    else:
        a_bs[a_b] = 1

    m_b_a = - b / a
    if m_b_a in m_b_as.keys():
        m_b_as[m_b_a] += 1
    else:
        m_b_as[m_b_a] = 1
    
    print(a_bs)
    print(m_b_as)
    print()

base = 1000000007
sm = 2**n % base

for a_b, cnt1 in a_bs.items():
    i_a_b = -(1/a_b)
    if -(1/a_b) in a_bs.keys():
        cnt2 = a_bs[i_a_b]
        sm -= ((cnt1+cnt2) * (2**(n-1) - 2**((n-1) - (cnt1+cnt2-1)))) % base

print(sm)
 
