# 파이썬 변수 동시 선언( 이렇게 해야하는거 처음 앎... )
m_col, m_row, lst_max = 0, 0, -1 # 최대값을 -1로 설정하는 이유는? 자연수 배열이므로 0이 최대 값일시 오류 발생 가능

for i in range(9):
  lst = list(map(int, input().split())) # 시간제한이 빡센 문제가 아니므로 반복문 내 input() 사용 가능
  for j in range(9):
    if lst[j] > lst_max:
      m_col = i + 1 # 리스트의 인덱스 값이므로 몇번째 인지 출력하기 위해 각 값에 + 1
      m_row = j + 1
      lst_max = lst[j]

print(lst_max) # 이차원 배열의 최대 값 출력
print(m_col, m_row) 