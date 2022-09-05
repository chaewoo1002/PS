n = int(input()) # 반복 횟수 입력

for i in range(n):
    score_list = list(map(int, input().split()))    # 입력을 한줄로 받으므로 list(map(int, input().split())) 메서드 사용, 0번 인덱스에는 학생 수 입력
    list_avg = sum(score_list[1:]) / score_list[0]  # 1번 인덱스부터 끝까지 값 더해서 학생수로 나눔 (평균 값 계산)
    people = 0                                      # 평균보다 높은 학생 수 선언
    for j in score_list[1:]:                        
        if j > list_avg:
            people += 1                             # 평균보다 높다면 people += 1
    per_people = people / score_list[0] * 100       # 평균 계산
    print(f"{per_people:.3f}%")                     # 평균 값 소수점 3번째까지 출력