l = int(input()) # 길이 입력

if l % 5 == 0 : # 5의 배수라면 5와 나눈 몫 출력
  print(l // 5)
else : # 아니라면 몫 + 1
  print(l // 5 + 1)