from collections import deque
import sys
queue = deque()
input = sys.stdin.readline
n = int(input())
for i in range(n):
    m = str(input())
    if m[:4] == 'push':
        queue.append(int(m[5:]))
    elif m == 'pop':
        try:
            print(queue[0])
            queue.popleft()
        except:
            print(-1)
    elif m == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif m == 'back':
        try:
            print(queue[-1])
        except:
            print(-1)
    elif m == 'size':
        print(len(queue))
    elif m == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)



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