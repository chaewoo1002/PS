findAlp = input() 
alpIndex = [0] * 26 # 값이 0으로 초기화 되어있는 리스트 26개 생성 (a ~ z)

for i in findAlp:
    alpIndex[ord(i)-97] += 1 # ord(문자)를 사용하면 문자의 유니코드 값을 반환한다. 알파벳 a는 97번째 글자이므로 -97을 하면 해당 글자 인덱스가 된다

print(*alpIndex) # 리스트가 초기화 되어있는 변수 앞에 *를 붙여 출력하면 해당 리스트 안의 값만 출력한다.