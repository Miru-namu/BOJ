#for문을 이용한 코드. range(n)이 n을 입력값으로 받기 때문에 다소 애매하다.
n = int(input())
num = 1
for i in range(n):
    num += 6*i
    if num >= n:
        print(i+1)
        break

#while문을 이용한 코드
n = int(input())
num = 1
i = 0

while True:
    num += 6*i
    i += 1 
    if num >= n:
        print(i)
        break