n = int(input())

feeling = 'I hate'
for i in range(n-1):
    feeling += ' that '
    
    if i%2 == 0:
        feeling += 'I love'
    else:
        feeling += 'I hate'

print(feeling+' it')