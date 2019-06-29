n = int(input())
D = [int(d) for d in input().split()]

sort_D = sorted(D)
mid = int(n / 2)
max_easy = sort_D[mid - 1]
min_difc = sort_D[mid]
print(min_difc - max_easy)
