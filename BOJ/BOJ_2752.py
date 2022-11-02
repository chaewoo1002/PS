num_lst = list(map(int, input().split())) # 3개의 값을 공백 기준으로 리스트에 삽입
num_lst.sort() # 리스트를 오름차순으로 정렬

for i in num_lst:
  print(i, end=" ")