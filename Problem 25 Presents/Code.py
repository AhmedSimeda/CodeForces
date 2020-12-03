n = int(input())
ps = input().split()

out = [0]*n
for i,p in enumerate(ps):
    out[int(p)-1] = str(i+1)

print(' '.join(out))