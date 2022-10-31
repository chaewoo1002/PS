h, m, s = map(int, input().split())
n = int(input())

s += n % 60
n = n // 60
if s >= 60: # 60초 이상이라면 1분 추가
    s -= 60
    m += 1

m += n % 60
n = n // 60
if m >= 60: # 60분 이상이라면 1시간 추가
    m -= 60
    h += 1

h += n % 24
if h >= 24: # 24시간을 초과한다면 -24시간
    h -= 24

print(h,m,s)