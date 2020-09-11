import math

a, b, h, m = map(int, input().split())

ang_a = (h+m/60)/12
ang_b = m/60
ang = ang_a - ang_b if ang_a - ang_b <= 0.5 else ang_b - ang_a
theta = ang * 2 * math.pi
print(math.sqrt(a**2 + b**2 - 2*a*b*math.cos(theta)))