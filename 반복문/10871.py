import sys
input = sys.stdin.readline
n, x = map(int, input().split())
nums = list(map(int, input().split()))
lst = [num for num in nums if num<x]
print(*lst, sep=' ')

# lst = ['1', '2', '3', '4']
# print(' '.join(lst))