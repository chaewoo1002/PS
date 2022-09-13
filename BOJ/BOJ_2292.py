n = int(input())

hoc = 1     # 벌집의 개수 (1부터 시작)
count = 1   # 실행 횟수, 1부터 시작하며 벌집 개수에 곱하기 위해 사용

while n > hoc:
    hoc += 6 * count    # 벌집의 개수는 6의 배수를 기준으로 늘어난다
    count += 1          # 1회 반복될때마다 실행횟수 += 1, 다음 벌집의 개수 (6 * count+1)개씩 추가

print(count)