# import sys
# input = sys.stdin.readline

# a, b = input().split()
# lst = list(map(int, input().split()))
# for _ in range(int(b)):
#     i, j = input().split()
#     print(sum(lst[int(i)-1:int(j)]))

# # 예제 입력 1 
# # 5 3
# # 5 4 3 2 1
# # 1 3
# # 2 4
# # 5 5
# # 예제 출력 1 
# # 12
# # 9
# # 1

import sys
import heapq
input = sys.stdin.readline

def heapsort(iterable):
    h = []
    result = []
    # 모든 원소를 차례대로 힙에 삽입
    for value in iterable:
        heapq.heappush(h, value)
    #힙에 삽입된 모든 원소를 차례대로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])
