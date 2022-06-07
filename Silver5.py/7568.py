import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    li=list(map(int,input().rstrip().split()))
    lst.append(li)
li.sort(key=lambda x:(x[0],x[1]))
cnt = 1
print(li)
for i in range(n):
    li[n-i-1]

