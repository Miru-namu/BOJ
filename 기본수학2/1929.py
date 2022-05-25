a, b = map(int, input().split())
lst=[]
for i in range(a,b):
    c = 2
    if a == 2:
        lst.append(2)
        pass
        for j in range(2,i):
            if a%j == 0:
                pass
            elif j == b-1:
                lst.append(j)
print(*lst, sep='\n')



# 예제 입력 1 
# 3 16
# 예제 출력 1 
# 3
# 5
# 7
# 11
# 13