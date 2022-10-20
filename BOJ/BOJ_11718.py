while True:
  try:
    print(input())
  except EOFError: # try except 구문은 정상적인 입력일때는 try가 실행되고 except(예외)가 발생하면 except문이 실행된다.
    break            # EOFError이 발생했다면? while: break