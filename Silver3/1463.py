n=int(input())
cnt = 0
while n > 1:
    if n%3 == 0:
        n /= 3
        cnt += 1
    elif n%3 == 1:
        n -= 1
        cnt += 1
    elif n%3 == 2:
        if n != 2:
            n -= 2
            cnt += 2
        else:
            cnt += 1
            break
    elif n%2 == 0:
        n /= 2
        cnt += 1
    elif n%2 == 1:
        n -= 1
        cnt += 1
    else:
        n -= 1
        cnt += 1
print(cnt)

d=[0]*(1000001)
print(d)

# # X가 3으로 나누어 떨어지면, 3으로 나눈다.
# # X가 2로 나누어 떨어지면, 2로 나눈다.
# # 1을 뺀다.
# # 정수 N이 주어졌을 때, 위와 같은 연산 세 개를 적절히 사용해서 1을 만들려고 한다. 연산을 사용하는 횟수의 최솟값을 출력하시오.

# # 입력
# # 첫째 줄에 1보다 크거나 같고, 106보다 작거나 같은 정수 N이 주어진다.

# # 출력
# # 첫째 줄에 연산을 하는 횟수의 최솟값을 출력한다.

# # 예제 입력 1 
# # 2
# # 예제 출력 1 
# # 1

# # 82 41 40 20 10 5 4 2 1 // 82 81 27 9 3 1
# # 163 162 54 18 6 3 1
# # 163 162 81 27 9 3 1 
# # 164 82 