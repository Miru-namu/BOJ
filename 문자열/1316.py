cnt = int(input())
# lst = []
sum = 0
for _ in range(cnt):
    word = input()
#     lst.append(word)

# for i in range(len(lst)):
#     word = list(lst[i])
    err = 0
    for i in range(len(word)-1):
        if word[i] != word[i+1]:
            new = word[i+1:]
            if new.count(word[i]) > 0:
                err += 1
    if err == 0:
        sum += 1
print(sum)

# 예제 입력 1 
# 3
# happy
# new
# year
# 예제 출력 1 
# 3
# 예제 입력 2 
# 4
# aba
# abab
# abcabc
# a
# 예제 출력 2 
# 1
# 예제 입력 3 
# 5
# ab
# aa
# aca
# ba
# bb
# 예제 출력 3 
# 4
# 예제 입력 4 
# 2
# yzyzy
# zyzyz
# 예제 출력 4 
# 0
# 예제 입력 5 
# 1
# z
# 예제 출력 5 
# 1