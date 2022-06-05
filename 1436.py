n=int(input())
cnt = 0
i=665
while n > cnt:
    i = i+1
    i = str(i)
    if i.count('666') > 0:
        cnt += 1
    i = int(i)
print(i)