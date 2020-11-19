distance_left = int(input())
steps = 5
moves = 0
while distance_left != 0:
    while steps > distance_left:
        steps -= 1
    for _ in range(distance_left//steps):
        distance_left -= steps
        moves += 1
    
print(moves)