n  = input()
stones = input()
out = ''
for i in range(len(stones)-1):
    if stones[i] == stones[i+1]:
        out += stones[i]

print(len(out))