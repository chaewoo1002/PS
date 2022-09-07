word = input().lower()      # 입력을 통일해서 받기 위해 모두 소문자로 입력
word_lst = list(set(word))  # set() 메서드를 사용해 중복을 제거한채 한개씩 리스트 안에 저장
count_lst = []              # 각 글자가 나온 만큼 횟수를 저장할 리스트 선언

for i in word_lst:      
    count = word.count(i)   # word_lst안의 글자가 나온 총 횟수를 count
    count_lst.append(count) # 구해진 count 값을 count_lst에 순차적으로 추가

if count_lst.count(max(count_lst)) >= 2: # 최대값이 2개 이상이라면 ? 
    print("?")

else:
    print(word_lst[(count_lst.index(max(count_lst)))].upper()) # count_lst의 최대값 인덱스를 찾아 word_lst의 값을 출력