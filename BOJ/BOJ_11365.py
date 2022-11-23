while True: # 한무 반복
  password = input()
  if password == 'END': # END가 입력되면 반복 종료
    break
  print(password[::-1]) # [::-1]을 문자열 뒤에 배치해주면 해당 문자열을 뒤집어 출력