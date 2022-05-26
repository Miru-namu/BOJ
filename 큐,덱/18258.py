from collections import deque

queue = deque()

n = int(input())
for i in range(n):
    queue.append(input().split())
    queue.popleft()


# 15
# push 1
# push 2
# front
# back
# size
# empty
# pop
# pop
# pop
# size
# empty
# pop
# push 3
# empty
# front
# 예제 출력 1 
# 1
# 2
# 2
# 0
# 1
# 2
# -1
# 0
# 1
# -1
# 0
# 3