while True:
  name, age, weight = input().split() # 이름, 나이, 몸무게 나눠서 입력 받기
  age, weight = int(age), int(weight)
  if name == '#' and age == 0 and weight == 0: # #, 0, 0이 입력되면 종료
      break

  if age > 17 or weight >= 80: # 17세가 넘거나, 몸무게가 80 이상이면 senior
      print(f"{name} Senior")

  else: # 그외 junior
      print(f"{name} Junior")