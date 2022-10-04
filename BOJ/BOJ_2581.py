fir_num = int(input()) # 줄바꿈 기준 입력을 받아야 하므로 입력 2줄 받기
end_num = int(input())

pnum_lst = [] # fir_num ~ end_num 사이의 소수를 저장할 리스트 생성

for i in range(fir_num, end_num + 1): # for _ in range(i, j)는 i ~ j-1 까지 반복하므로 end_num에 1을 더해준다
  div_num = 0
  if i > 1:
    for j in range(2, i):
      if i % j == 0:
        div_num += 1
        break
    if div_num == 0:
      pnum_lst.append(i) # 나눠지는 수의 개수가 0개라면 소수 리스트에 추가

if len(pnum_lst) > 0: # 소수 리스트의 길이가 0보다 크면?
  print(sum(pnum_lst))  # 리스트 내의 값 총 합과
  print(min(pnum_lst))  # 리스트 내의 값 중 가장 작은 값을 출력
else:
  print(-1) # 소수 리스트의 길이가 0보다 작거나 같다면 -1 출력