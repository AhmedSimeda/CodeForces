n = int(input())
passengers = 0
capacity = 0
for _ in range(n):
    exit, enter = tuple(map(int,input().split()))
    passengers = passengers - exit + enter
    if passengers > capacity:
        capacity = passengers
    
print(capacity)