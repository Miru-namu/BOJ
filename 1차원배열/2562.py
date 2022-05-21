# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# 예제 입력 1 
# 3
# 29
# 38
# 12
# 57
# 74
# 40
# 85
# 61
# 예제 출력 1 
# 85
# 8

import sys
input = sys.stdin.readline
lst = []
for _ in range(9):
    num = int(input())
    lst.append(num)
idx = [i for i in range(9) if max(lst) == lst[i]]
print(max(lst))
print(int(*idx)+1, sep='')