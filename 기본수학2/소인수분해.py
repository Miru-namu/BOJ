# 11653
n = int(input())
m = n
if n == 1:
    exit(0)

else:
    while True:
        for i in range(2,int(m)+1):
            if n%i == 0:
                print(i)
                n = int(n)/int(i)
                break
            elif n == 1:
                exit(0)
        
        



# 예제 입력 1 
# 72
# 예제 출력 1 
# 2
# 2
# 2
# 3
# 3
# 예제 입력 2 
# 3
# 예제 출력 2 
# 3
# 예제 입력 3 
# 6
# 예제 출력 3 
# 2
# 3
# 예제 입력 4 
# 2
# 예제 출력 4 
# 2
# 예제 입력 5 
# 9991
# 예제 출력 5 
# 97
# 103