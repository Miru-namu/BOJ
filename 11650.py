li = []
n=int(input())
for i in range(n):
    a, b = map(int,input().split())
    li.append((a,b))
li.sort()
for i in range(n):
    print(li[i][0],li[i][1])