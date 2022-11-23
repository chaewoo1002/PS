month = int(input())
day = int(input())
if month == 2 and day == 18: # 2월 18일이면 special 출력
    print('Special')
elif month == 2:
  print('After' if day > 18 else 'Before') # 2월이면서 18일 이전이면 before, 이후라면 after 출력
elif month > 2: # 2월 이후면 after
    print('After')
elif month < 2: # 2월 이전이면 before
    print('Before')