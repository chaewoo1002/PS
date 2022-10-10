while True: # 조건을 만족할때까지 반복
    try: # 실행한 코드가 오류가 없는지 확인
        n, s = map(int, input().split()) # n, s값 저장
        print(s // (n+1))  
    except EOFError: # 입력값이 EOF(End Of the File)이라면
        break         # 반복 종료