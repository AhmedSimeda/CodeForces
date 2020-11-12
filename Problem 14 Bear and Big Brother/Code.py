Limak, Bob = list(map(int,input().split()))
years = 0
while Limak <= Bob:
    years += 1
    Limak *= 3
    Bob   *= 2
print(years)