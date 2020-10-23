n = int(input())
sols = 0
for _ in range(n):
    friends = input()
    if friends.count('1') >= 2:
        sols += 1

print(sols)