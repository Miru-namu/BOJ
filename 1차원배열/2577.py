# 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다. 마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

# 예제 입력 1 
# 150
# 266
# 427
# 예제 출력 1 
# 3
# 1
# 0
# 2
# 0
# 0
# 0
# 2
# 0
# 0

import sys
input = sys.stdin.readline
a = int(input())
b = int(input())
c = int(input())
d = a*b*c
num_list = list(map(int, str(d)))

print(num_list.count(0))
print(num_list.count(1))
print(num_list.count(2))
print(num_list.count(3))
print(num_list.count(4))
print(num_list.count(5))
print(num_list.count(6))
print(num_list.count(7))
print(num_list.count(8))
print(num_list.count(9))

#숏코딩
# a=input;A=int(a());B=int(a());C=int(a())
# for i in range(10): print(str(A*B*C).count(str(i)))

# len0 = 0
# len1 = 0

# lst = [1, 1, 2, 4, 5, 0, 0, 8]
# for i in range(10):
#     global()["len{}".format(i)]

# def cnt(lst):
#     lst
#     len