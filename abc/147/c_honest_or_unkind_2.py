N = int(input())
A = list()
E = list()
for i in range(N):
    A.append(int(input()))
    evid = list()
    for j in range(A[-1]):
        target, label = input().split()
        evid.append([int(target) - 1, int(label)])
    E.append(evid)

max_honesty = 0
for i in range(2**N):
    state = [(i >> j) & 1 for j in range(N)]
    is_contrad = False
    for j in range(N):
        if state[j] == 1:
            evids = E[j]
            for e in  evids:
                target, label = e
                if label != state[target]:
                    is_contrad = True
                    break
        if is_contrad:
            break
    if not is_contrad and max_honesty < sum(state):
        max_honesty = sum(state)

print(max_honesty)
