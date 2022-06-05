l, w = map(int, input().split())
li = []
for _ in range(l):
    li.append(input())

nums = []
for i in range(l-7):
    for j in range(w-7):
        B_cnt = 0
        W_cnt = 0
        for a in range(8):
            for b in range(8):
                if a+i+b+j % 2 != 0:
                    if li[a+i][b+j] == 'B':
                        B_cnt += 1
                    elif li[a+i][b+j] == 'W':
                        W_cnt += 1
                elif a+i+b+j % 2 == 0:
                    if li[a+i][b+j] == 'B':
                        W_cnt += 1
                    elif li[a+i][b+j] == 'W':
                        B_cnt += 1
        nums.append(B_cnt)
        nums.append(W_cnt)
print(min(nums))




