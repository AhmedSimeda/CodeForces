str1 = input().lower()
str2 = input().lower()
order = sorted([str1,str2])
if str1 == str2:
    print(0)
elif order[0] == str1:
    print(-1)
else:
    print(1)