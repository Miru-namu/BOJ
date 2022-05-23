import sys
input = sys.stdin.readline
lst = []
a, b, c, d = map(int, input().split())
lst.append(a)
lst.append(b)
lst.append(c-a)
lst.append(d-b)
print(min(lst))
# 예제 입력 1 
# 6 2 10 3
# 예제 출력 1 
# 1
# 예제 입력 2 
# 1 1 5 5
# 예제 출력 2 
# 1
# 예제 입력 3 
# 653 375 1000 1000
# 예제 출력 3 
# 347
# 예제 입력 4 
# 161 181 762 375
# 예제 출력 4 
# 161