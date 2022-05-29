# 예제 입력 2 
# 10 4790
# 1
# 5
# 10
# 50
# 100
# 500
# 1000
# 5000
# 10000
# 50000
# 예제 출력 2 
# 12

a, b = map(int, input().split())

lst = []
cnt = 0
for i in range(a):
    coin = int(input())
    lst.append(coin)

while lst[-1] > coin:
    lst.pop()

while b > 0:
    if lst[-1] > b:
        lst.pop()
    elif lst[-1] == b:
        b = b-lst[-1]
        cnt += 1
    elif lst[-1] < b:
        i = b//lst[-1]
        b = b-lst[-1]*i
        cnt += i
    else:
        print('Error')
        exit(0)

print(cnt)