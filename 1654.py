import sys
input = sys.stdin.readline
a,b=map(int,input().rstrip().split())
lst = []
for _ in range(a):
    lst.append(int(input()))
result = []
while True:
    for i in range(1,min(lst)+1):
        li=[]
        cnt=0
        for j in lst:
            li.append(j//i)
        cnt = sum(li)
        if cnt == b:
            result.append(i)
    if i == min(lst):
            break
print(max(result))