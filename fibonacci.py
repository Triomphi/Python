def fib(number):
    if number == 0:
        return 0
    elif number == 1 or number == 2:
        return 1
    elif number > 2 :
        a = 1
        b = 1
        for i in range (3, number+1):
            c = a+b
            a,b = b,c
        return c
    
