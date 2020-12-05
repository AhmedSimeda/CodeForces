h = int(input().split()[1])
friends = [int(f) for f in input().split()]

print(sum([1 if f<= h else 2 for f in friends]))