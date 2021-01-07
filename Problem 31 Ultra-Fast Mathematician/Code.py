def XOR(num1, num2):
    out = ''
    for n1, n2 in zip(num1, num2):
        if n1 != n2:
            out += '1'   
        else:
            out += '0'
    print(out)
    
num1  = input()
num2  = input()

XOR(num1, num2)