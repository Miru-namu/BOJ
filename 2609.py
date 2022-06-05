a,b = map(int, input().split())
lst=[]
lst2=[]
while True:
    if lst2.count(a) > 0:
        break
    for i in range(2,min(a,b)+1):
        if a%i == 0 and b%i == 0:
            a=a//i
            b=b//i
            lst.append(i)
            break
        elif i == min(a,b):
            lst2.append(a)
            lst2.append(b)
c=1          
for i in lst:
    c = c*i
print(c)
d=1
for i in lst2:
    d = d*i
print(c*d)
    

    


# 예제 입력 1 
# 24 18
# 예제 출력 1 
# 6
# 72