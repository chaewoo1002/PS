k, n, m = map(int, input().split()) # 과자 1개의 가격 k, 구매 개수 n, 현재 가진 돈 m

res = k*n - m # 더 필요한 돈의 액수 = 과자1개의 개수 * 구매 개수 - 현재 가진 돈

if res >= 0: # 0보다 크다면 결과 값 출력
  print(res)
else: # 0보다 적을시 현재 가진 돈의 양이 많으므로 0 출력 
  print(0)