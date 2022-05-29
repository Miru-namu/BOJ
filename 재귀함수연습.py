def GCD(num1, num2):
    if num1%num2 == 0:
        return print(num2)
    return GCD(num2,num1%num2)

def fac(n):
    if n == 0:
        return 1
    return n * fac(n-1)

print(fac(10))