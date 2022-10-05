n = int(input())

for i in range(2, n+1):
    while n%i == 0: # 나눈 후의 나머지가 0이라면 나누기가 가능한 수이므로 출력
        print(i) 
        n//=i # 출력 후에 n의 값 나눈 수만큼 나눈 후 값 재저장
    if n == 1:  # n의 값이 1이라면?
        break   # 소인수 분해가 완료 된 상태이므로 반복 종료.