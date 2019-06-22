N, K = [int(e) for e in input().split()]
A = [int(a) for a in input().split()]

count = 0
sumA = sum(A)

if sumA < K:
    print(0)
else:
    count += 1
    now = sumA
    for a in A:
        now -= a

        now2 = now
        for a in reversed(A):
            now2 -= a
            if now2 < K:
                break
            else:
                count += 1

        if now < K:
            break
        else:
            count += 1

    now = sumA
    for a in reversed(A):
        now -= a
        if now < K:
            break
        else:
            count += 1
    print(count)


def check(count, A):
    if sum(A) < K:
        return count, A
    elif len(A) == 1:
        return count + 1, A
    count += check(count, A[1:])[0]
    return check(count + 1, A[:-1])

a, _ = check(0, A)
print("a:", a)

A.reverse()
b, _ = check(0, A)
print("b:", b)
print(a + b - 1)
