def f(n):
    # sum of even_numbers
    ## first of all we need to determine n_even, a_1, a_n
    n_even, a_1, a_n = n//2, 2, n if n%2==0 else n-1
    even_sum = n_even*((a_1+a_n)//2)
    
    # similarly let's get the sum of odd numbers
    n_odd, a_1, a_n  = n-n//2, 1, n if n%2!=0 else n-1
    odd_sum  = n_odd*((a_1+a_n)//2)
    
    print(even_sum - odd_sum)
    
f(int(input()))