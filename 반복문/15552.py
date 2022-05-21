# https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline
# https://www.acmicpc.net/board/view/22716
# 참고로 이름이 꽤 길기 때문에 저는 input = sys.stdin.readline을 맨 처음에 함으로써 쓰는 편입니다.

import sys
input = sys.stdin.readline
cnt = int(input())

for i in range(cnt):
    a, b = map(int, input().split())
    print(a+b)