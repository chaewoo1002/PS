scoreList = [] # 점수 리스트

for i in range(5):
  scoreList.append(int(input()))
  if scoreList[i] <= 40: # 점수가 40점 미만이라면 최소 점수인 40점으로 초기화
    scoreList[i] = 40

print(sum(scoreList) // 5) # 점수 리스트의 총합을 5로 나눈 값(평균) 출력