n = int(input())
groups = 1
prev = 'Ahmed'    #anything other than '01' and '10'
for _ in range(n):
    curr = input()
    if prev[-1] == curr[0]:
        groups += 1
    prev = curr

print(groups)