n = int(input())
available = 0

for _ in range(n):
    p,q = list(map(int, input().split()))
    if q-p >= 2:
        available += 1

print(available)