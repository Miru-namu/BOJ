a, b, c = map(int, input().split())
if b >= c:
    print(-1)
else:
    print(1+a//(c-b))