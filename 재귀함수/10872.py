def fac(n):
    a = 1
    if n == 0:
        print(1)
        exit(0)
    for i in range(1,n+1):
        a = a*i
    return a
num = int(input())
print(fac(num))