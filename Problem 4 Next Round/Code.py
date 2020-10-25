info = list(map(int,input().split()))
players = list(map(int,input().split()))
wins = sum(map(lambda x: (x >= players[info[1]-1]) and (x > 0),players))
print(wins)