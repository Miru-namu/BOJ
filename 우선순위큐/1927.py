import sys
import heapq
input = sys.stdin.readline

heap = []
n = int(input())
for i in range(n):
    m = int(input())
    if m == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))
    else:
        heapq.heappush(heap,m)


# 출력
# 입력에서 0이 주어진 횟수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

# 예제 입력 1 
# 9
# 0
# 12345678
# 1
# 2
# 0
# 0
# 0
# 0
# 32
# 예제 출력 1 
# 0
# 1
# 2
# 12345678
# 0

# #3.1 priority Queue
# import heapq
# heap = []

# #heap 리스트 안에 요소 추가
# heapq.heappush(heap, value)

# #heap 리스트를 heapq 타입으로 변환
# heapq.heapify(heap)

# #heapq타입의 변수를 heappop()의 인자로 집어넣으면 가장 작은값의 원소를 삭제후 리턴함
# heap = [1, 2, 7, 3, 4]
# print(heapq.heappop(heap)) # 1
# print(heap) # [2, 3, 7, 4]

# #최대 힙 표현
# reverse_sign = lambda x: x*-1
# max_heap = list(map(reverse_sign, _list))
# heapq.heapify(max_heap)
# max_heap = list(map(reverse_sign, max_heap))

