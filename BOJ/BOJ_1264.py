while True:
    n = input()
    if n == '#': # '#'이 입력되면 종료
        break
    cnt = 0
    for c in n:
        if c in 'aeiouAEIOU': # 문자열을 통해 확인
            cnt += 1
    print(cnt)