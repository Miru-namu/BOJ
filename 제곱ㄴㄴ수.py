# from collections import deque
# import heapq
# import sys
# a, b = map(int, sys.stdin.readline().rstrip().split())

# lst = deque([4])
# for i in range(2,round(b**(1/2))+1):
#     for j in range(2,i):
#         if i%j == 0:
#             break
#         elif j == i-1:
#             lst.append(i**2)

# result = deque()
# for i in range(a, b+1):
#     for j in lst:
#         if j > i:
#             break
#         elif i%j == 0:
#             result.append(i)
#             break

# print(b+1-a-len(result))


# # heap = []
# # for _ in range(a,b+1):
# #     heapq.heappush(heap,_)

# # lst = [4]
# # for i in range(2,round(b**(1/2))+1):
# #     for j in range(2,i):
# #         if i%j == 0:
# #             break
# #         elif j == i-1:
# #             heapq.heappush(lst,i**2)

# # result = []
# # for i in range(a, b+1):
# #     for j in lst:
# #         if j > i:
# #             break
# #         elif i%j == 0:
# #             heapq.heappush(result,i)
# #             break

# # print(b+1-a-len(result))

# # print(lst)
# # print(result)

# # # set(result)
# # # 1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
# # # 4,9,16,25
# # # result [4,8,9,12,16,18,20]
# # # print(lst)

import sys
input = sys.stdin.readline
def solution(MIN,MAX):
    answer = MAX-MIN+1
    check = [False]*(MAX-MIN+1)
    i=2
    while i*i <= MAX:
        square_number = i*i #제곱수
        # remain
        # 제곱수가 딱 나누어 떨어지면 상관없지만 그게 아니라면 소수점이 버림 처리 된다.
        # 그래서 remain으로 그 값을 보정해준다.
        remain = 0 if MIN%square_number==0 else 1
        j = MIN//square_number + remain #제곱수로 나눈 몫 => 배수
        while square_number*j <= MAX:   #제곱수의 j배 (에라토스테네스의 체)
            if not check[square_number*j-MIN]:
                check[square_number*j-MIN]=True
                answer-=1
            j+=1#배수 점점 증가
        i+=1        
    print(answer)
a,b = map(int,input().split())
solution(a,b)

https://my-coding-notes.tistory.com/86

minn, maxx = map(int,input().split())
a = [i**2 for i in range(2,int(maxx**0.5)+1)]
num = [1] * (maxx-minn+1)
for i in a:
    n = minn//i*i
    while(n < maxx+1):
        if n - minn >= 0:
            num[n-minn] = 0
        n += i
print(sum(num))