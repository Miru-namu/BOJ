import sys
input = sys.stdin.readline

a, b = input().split()
lst = list(map(int, input().split()))
for _ in range(int(b)):
    i, j = input().split()
    print(sum(lst[int(i)-1:int(j)]))

# 예제 입력 1 
# 5 3
# 5 4 3 2 1
# 1 3
# 2 4
# 5 5
# 예제 출력 1 
# 12
# 9
# 1
