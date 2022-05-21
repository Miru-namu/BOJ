# 첫째 줄에 두 정수 H와 M이 주어진다. (0 ≤ H ≤ 23, 0 ≤ M ≤ 59) 그리고 이것은 현재 상근이가 설정한 놓은 알람 시간 H시 M분을 의미한다.

# 입력 시간은 24시간 표현을 사용한다. 24시간 표현에서 하루의 시작은 0:0(자정)이고, 끝은 23:59(다음날 자정 1분 전)이다. 시간을 나타낼 때, 불필요한 0은 사용하지 않는다.

h, m = map(int,input().split())

sum_min = h*60+m

if sum_min > 1440 and sum_min < 60:
    sum_min = sum_min%60

clock_sum = sum_min - 45
clock_h = clock_sum//60
if clock_h < 0:
    clock_h = 23
clock_m = clock_sum%60

print(clock_h,clock_m)