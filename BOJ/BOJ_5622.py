dial = input()
dial_list = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]

sec = 0
for unit in dial_list :  
    for i in unit:  # alpabet 리스트에서 각 요소를 꺼내서 한글자씩 분리
        for x in dial :  # 입력받은 문자를 하나씩 분리
            if i == x :  # 두 알파벳이 같으면
                sec += dial_list.index(unit) +3  # time = time + index +3
print(sec)