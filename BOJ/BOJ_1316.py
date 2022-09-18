# 참고 : https://velog.io/@jiyeah3108/Python-%EB%B0%B1%EC%A4%80-1316%EB%B2%88-%EA%B7%B8%EB%A3%B9-%EB%8B%A8%EC%96%B4-%EC%B2%B4%EC%BB%A4

groupWord = 0     # 출력할 그룹 단어의 개수
n = int(input())  # 입력될 단어의 개수 입력

for i in range(n):  # 입력될 단어의 개수만큼 반복
    word = input()  # 단어 입력
    for j in range(len(word) - 1):  
        if word[j] != word[j+1]:    # j인덱스 값의 문자와 j+1 인덱스 값의 문자가 다르다면 ?
            new = word[j+1 : ]      # j+1부터 단어끝까지를 new에 초기화
            if word[j] in new:      # word j가 new안에 포함되어 있다면? 
                groupWord -= 1          # ㄴ> 그룹 단어가 아니므로 groupWord -1
                break                   # 반복 종료
    groupWord += 1                  # 반복 한개당 그룹 단어의 개수 + 1

print(groupWord)    # 그룹 단어의 개수 출력