word_lst = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']    # 크로아티아 글자 리스트 생성

word = input()

for i in word_lst:
    word = word.replace(i, 'a')     # 크로아티아 글자 리스트 안의 글자와 동일한 글자가 있다면? -> 'a'로 replace해서 저장
print(len(word))                    # word 문자열의 길이 출력 == 몇개의 크로아티아 글자로 이루어져있는지 출력