n = int(input())

for i in range(n):
    time, str = input().split()         # 반복 횟수, str은 반복할 글자 입력
    for j in str:
        print(j * int(time), end="")    # print문 안에 출력할 값 다음으로 쉼표로 구분후 end = ""을 해주면 공백 없이 출력을 한다
    print()                             # end = ""을 사용해 줄바꿈이 사라진 상태이므로 임의의 print문을 사용하여 줄바꿈 생성