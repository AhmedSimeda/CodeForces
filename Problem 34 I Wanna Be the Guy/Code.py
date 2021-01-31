levels, x, y = int(input()), set(map(int,input().split()[1:])), set(map(int,input().split()[1:]))

print("I become the guy." if len(set(range(1,levels+1))-(x|y)) == 0 else "Oh, my keyboard!")