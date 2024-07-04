

#Base Case
#Recursive Case

#fac(5) 5 * 4 * 3 * 2 * 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    
print(factorial(5))

def while_fac(n):
    factorial = 1
    while n > 1:
        factorial *= n
        n -= 1

    return factorial