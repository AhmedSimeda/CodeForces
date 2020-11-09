k,n,w = list(map(int,input().split()))
overall = sum([i*k for i in range(1,w+1)])
print(max(0,overall-n))