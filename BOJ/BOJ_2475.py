inh_numlst = list(map(int, input().split())) # 고유번호(inherence number)리스트 입력

res = 0 # 출력 값을 저장할 변수 선언 및 초기화
for i in inh_numlst:
  res += i**2 # res에 고유번호 리스트 내의 i번 인덱스 값 ** 2(i의 제곱) 만큼 더함 

print(res % 10) # 검증수를 출력하기 위해 결과값에 10으로 나눈 나머지 출력