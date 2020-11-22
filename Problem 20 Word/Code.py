word = input()
letters = [chr(i) for i in range(65,91)]
upper = [w for w in word if w in letters]
if len(upper) > (len(word)-len(upper)):
    print(word.upper())
else:
    print(word.lower())