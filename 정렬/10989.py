import sys
input = sys.stdin.readline
n=int(input())
li = [0]*10000001
for i in range(n):
    li[int(input())] += 1

for i in range(10000001):
    if li[i] != 0:
        for j in range(li[i]):
            print(i)