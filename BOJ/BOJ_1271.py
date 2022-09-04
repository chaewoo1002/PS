# 기존 코드

# money = int(input())
# life = int(input())

# print(money // life)
# print(money % life)

# 수정 코드

money, life = map(int, input().split()) # 한줄에 입력을 모두 받으므로 input().split()을 사용해서 값을 나눠주고  
                                        # map 메서드를 사용해 값을 각각 money, life에 저장해준다

print(money // life) # 돈을 생명체의 개수로 나눈 값 출력
print(money % life) # 나누고 난 후 남은 돈 출력

# 기존 코드 제출시 런타임 에러가 발생 
#   ㄴ> 왜? 문제에서의 입력은 한줄로 주어지지만 입력을 두줄로 나눠서 받으려 했기 때문에
#       ㄴ> map(int,input().split()) 메서드를 통해 해결 (정답코드 참고)