k, l, m, n, d = int(input()), int(input()), int(input()), int(input()), int(input())
harmed = set(range(k,d+1,k)) | set(range(l,d+1,l)) | set(range(m,d+1,m)) | set(range(n,d+1,n))

print(len(harmed))  #unharmed