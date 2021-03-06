from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
queue = deque()

for i in range(n):
    command = list(input().split())
    if command[0] == 'push_back':
        queue.append(command[1])
    elif command[0] == 'push_front':
            queue.appendleft(command[1])
    elif command[0] == 'pop_back':
        try:
            print(queue.pop())
        except:
            print(-1)
    elif command[0] == 'pop_front':
        try:
            print(queue.popleft())
        except:
            print(-1)
    elif command[0] == 'front':
        try:
            print(queue[0])
        except:
            print(-1)
    elif command[0] == 'back':
        try:
            print(queue[len(queue)-1])
        except:
            print(-1)
    elif command[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif command[0] == 'size':
        print(len(queue))

# 명령은 총 여덟 가지이다.

# push_front X: 정수 X를 덱의 앞에 넣는다.
# push_back X: 정수 X를 덱의 뒤에 넣는다.
# pop_front: 덱의 가장 앞에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# pop_back: 덱의 가장 뒤에 있는 수를 빼고, 그 수를 출력한다. 만약, 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# size: 덱에 들어있는 정수의 개수를 출력한다.
# empty: 덱이 비어있으면 1을, 아니면 0을 출력한다.
# front: 덱의 가장 앞에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# back: 덱의 가장 뒤에 있는 정수를 출력한다. 만약 덱에 들어있는 정수가 없는 경우에는 -1을 출력한다.
# 입력
# 첫째 줄에 주어지는 명령의 수 N (1 ≤ N ≤ 10,000)이 주어진다. 둘째 줄부터 N개의 줄에는 명령이 하나씩 주어진다. 주어지는 정수는 1보다 크거나 같고, 100,000보다 작거나 같다. 문제에 나와있지 않은 명령이 주어지는 경우는 없다.

# 출력
# 출력해야하는 명령이 주어질 때마다, 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 15
# push_back 1
# push_front 2
# front
# back
# size
# empty
# pop_front
# pop_back
# pop_front
# size
# empty
# pop_back
# push_front 3
# empty
# front
# 예제 출력 1 
# 2
# 1
# 2
# 0

# 2
# 1
# -1
# 0
# 1
# -1
# 0
# 3