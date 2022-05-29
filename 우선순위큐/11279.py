# 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 큰 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# 예제 입력 1 
# 13
# 0
# 1
# 2
# 0
# 0
# 3
# 2
# 1
# 0
# 0
# 0
# 0
# 0
# 예제 출력 1 
# 0
# 2
# 1
# 3
# 2
# 1
# 0
# 0

import sys
import heapq

input = sys.stdin.readline

n = int(input())

def heapsort(iterable):
    h = []
    result = []
    for value in iterable:
        heapq.heappush(h, -value)
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

heap = []
heapq.heapify(heap)

for i in range(n):
    m = int(input())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            heapsort(heap)
            print(heapq.heappop(heap))
            heapsort(heap)
    else:
        heapq.heappush(heap,m)