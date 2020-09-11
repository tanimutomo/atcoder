x = int(input())

is_found = False
for i in range(-500, 501):
    for j in range(-500, 501):
        if i**5 - j**5 == x:
            print(i, j)
            is_found = True
        if is_found:
            break
    if is_found:
        break