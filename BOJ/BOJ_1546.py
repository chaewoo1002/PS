# 파이썬에서 리스트의 평균값을 편리하게 구하기 위해 statistics 모듈을 import 해준다.
import statistics

count = int(input())
scr = list(map(int, input().split()))
new_scr = []

# for문을 사용하여 기존 점수 리스트의 값을 호출, 새로운 값으로 변경하여 new_scr에 값을 추가해준다.
for i in range(len(scr)):
    new_scr.append(scr[i] / max(scr) * 100)

# 평균값을 avg 변수에 초기화
avg = statistics.mean(new_scr)

print(avg)