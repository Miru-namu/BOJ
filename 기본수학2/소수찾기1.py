cnt = int(input())
nums = list(map(int, input().split()))

result = 0
for num in nums:
    if num == 2:
        result += 1
    for j in range(2,num):
        if num%j == 0:
            break
        elif j == num-1:
            result += 1
print(result)

# 2 3 5 7

# 1 0
# 2 1
# 3 1
# 4