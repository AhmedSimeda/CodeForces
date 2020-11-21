number = input()
sevens = number.count('7')
fours = number.count('4')
if sevens+fours in [7,4]:
    print("YES")
else:
    print("NO")