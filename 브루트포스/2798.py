# 예제 입력 1 
# 5 21
# 5 6 7 8 9
# 예제 출력 1 
# 21
# 예제 입력 2 
# 10 500
# 93 181 245 214 315 36 185 138 216 295
# 예제 출력 2 
# 497

a , b = map(int, input().split())
lst = list(map(int, input().split()))
for i in range(len(lst)):
    lst[i]