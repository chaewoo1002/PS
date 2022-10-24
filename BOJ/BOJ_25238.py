arm, per = map(int, input().split()) # 공백 기준 입력 나눠 받기

if (arm - (arm * (per * 0.01))) < 100: # 방어력 - (방어력 * 체감 방어율) = 실제 방여력 이므로 이 수차가 100보다 낮으면 1 출력
  print(1)
else:
  print(0)