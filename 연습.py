import sys
input = sys.stdin.readline
a,b=map(int,input().split())
nums=list(map(int,input().split()))
lst = [0]
cnt = 0
for i in nums:
    cnt += i
    lst.append(cnt)

for j in range(b):
    x,y=map(int,input().split())
    print(lst[y]-lst[x-1])

# print(lst)

# for i in range(b):