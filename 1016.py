m = int(input())
def han(n):
    cnt = 0
    for i in range(1,n+1):
        if i<100:
            cnt += 1
        elif i>=100 and i<=1000:
            a=i//100
            b=(i//10)%10
            c=i%10
            if a-b == b-c:
                cnt += 1
    return cnt

print(han(m))


