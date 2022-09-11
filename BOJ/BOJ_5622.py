dial = input()
dial_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

sec = 0
for num in dial_list :  
    for i in num:           # dial_list에서 값을 꺼내서 한글자씩 분리
        for j in dial :     # 입력받은 문자를 한글자씩 분리
            if i == j :  
                sec += dial_list.index(num) + 3   # 입력받은 문자와 dial_list의 값이 일치할때 다이얼리스트의 인덱스값 +3 만큼을 시간에 추가
print(sec)