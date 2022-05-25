def countdown(n):
    if n == 0:
        print("Blastoff!")
    else:
        print(n)
        countdown(n-1)

def power(x, n):
    if n == 0:
        return 1
    return x * power(x, n-1)

power(2,10)

n = int(input())

