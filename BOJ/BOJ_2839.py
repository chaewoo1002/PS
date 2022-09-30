sugar = int(input()) # 설탕의 개수 입력

res = 0 # 설탕 봉지의 수

while sugar >= 0:
    if sugar % 5 == 0: # 설탕 개수가 5로 나누어 떨어지는 경우
        res += sugar // 5 # 5로 나눈 몫 추력
        print(res)
        break
    sugar -= 3 # 설탕이 5의 배수가 될때까지 반복
    res += 1
else:
    print(-1) # while문을 벗어나게 되면 -1 출력. 3과 5의 배수합이 아님을 의미