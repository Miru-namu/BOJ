# 출력
# 첫째 줄에 입력으로 주어진 M개의 수에 대해서, 각 수가 적힌 숫자 카드를 상근이가 가지고 있으면 1을, 아니면 0을 공백으로 구분해 출력한다.

# 예제 입력 1 
# 5
# 6 3 2 10 -10
# 8
# 10 9 -5 2 3 4 5 -10
# 예제 출력 1 
# 1 0 0 1 1 0 0 1
import sys
input = sys.stdin.readline

n = int(input())
li_1 = list(map(int, input().split()))
m = int(input())
li_2 = list(map(int, input().split()))
result = []
for i in li_2:
    for j in li_1:
        if i == j:
            result.append(1)
            break
        elif j == li_1[len(li_1)-1]:
            result.append(0)
        else:
            pass
print(*result)