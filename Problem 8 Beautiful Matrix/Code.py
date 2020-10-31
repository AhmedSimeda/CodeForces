for r in range(5):
    m = list(map(int,input().split()))
    if 1 in m:
        row = r+1
        col = m.index(1)+1
print(abs(3-col)+abs(3-row))   