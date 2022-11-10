a, b = map(int, input().split())
peopleList = list(map(int, input().split())) # 파티 참가자 리스트 생성
party = a * b # 파티장 크기 입력
for i in peopleList:
    print(i - party, end=' ') # 실제 인원과 오차 범위 출력