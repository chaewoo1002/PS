n = int(input())


for i in range(0, n): # 입력 받은 횟수만큼 반복
    score, point = 0, 1 # score는 출력될 점수를 의미, point는 'O'가 입력되었을때 score에 더해지는 점수를 의미한다
    lst = list(input()) # 'O','X'를 입력받을 리스트 생성
    for j in lst:
        if (j == 'O'): # 리스트 내의 j번째 인덱스의 값이 'O'라면
            score += point # point만큼의 점수를 score에 더함
            point += 1 # 연속으로 'O'가 입력되었을때의 점수 계산을 위해 point의 값을 1 더해줌
        else:
            point = 1 # 'X'가 입력되었다면 현재 point의 저장된 값을 1로 초기화 시키고 다시 반복문으로
    print(score) 