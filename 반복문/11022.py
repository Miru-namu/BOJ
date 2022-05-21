import sys
input = sys.stdin.readline

cnt = int(input())
for i in range(cnt):
    a, b = map(int, input().split())
    print('Case #'+str(i+1)+':',str(a),'+',str(b),'=',str(a+b))