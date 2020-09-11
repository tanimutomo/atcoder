import sys

N = int(input())
tasks = []
for i in range(N):
    time, dead = [int(i) for i in input().split()]
    tasks.append([time, dead])

tasks = sorted(tasks, key=lambda task: task[1])

now = 0
for time, dead in tasks:
    now += time
    if now > dead:
        print("No")
        sys.exit()
print("Yes")
