balance = sum(map(int, input().split())) # 두 통장의 잔액(balance) 합
chicken = int(input()) # 치킨 한마리의 가격

if balance >= chicken*2: # 안타깝게도 욱재는 치킨을 두마리 사야한다.
  print(balance - chicken*2)
else: # 안된다면 잔고 출력
  print(balance)