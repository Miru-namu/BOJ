# 26부터 시작한다. 2+6 = 8이다. 새로운 수는 68이다. 6+8 = 14이다. 새로운 수는 84이다. 8+4 = 12이다. 새로운 수는 42이다. 4+2 = 6이다. 새로운 수는 26이다.

# 위의 예는 4번만에 원래 수로 돌아올 수 있다. 따라서 26의 사이클의 길이는 4이다.

# N이 주어졌을 때, N의 사이클의 길이를 구하는 프로그램을 작성하시오.

# 예제 입력 1 
# 26
# 예제 출력 1 
# 4
# 예제 입력 2 
# 55
# 예제 출력 2 
# 3
# 예제 입력 3 
# 1
# 예제 출력 3 
# 60
# 예제 입력 4 
# 0
# 예제 출력 4 
# 1
# 예제 입력 5 
# 71
# 예제 출력 5 
# 12

import sys
input = sys.stdin.readline
num = int(input())
num2 = num

try_num = 0
while True:
    try_num += 1
    a = num//10
    b = num%10
    c = (a+b)
    d = b*10+c%10
    num = d
    if num2 == num:
        break
print(try_num)

# 02 + 06 = 08
# 68
# 06 + 08 = 14
# 84
# 08 + 04 = 12
# 42
# 04 + 02 = 06
# 26