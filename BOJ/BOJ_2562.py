arr = [int(input()) for i in range(9)]
'''
이 문제의 경우 입력이 줄바꿈 처리되어 총 9개 입력된다 num_list = list(map(int, input().split())) 메서드를 사용하면
줄바꿈 입력을 받지 못하기 때문에 구글이 알려준 arr = [int(input()) for _ in range(n)] 메서드를 사용해 반복문과 줄바꿈 입력을
한줄 코드로 사용할 수 있다.
'''

# 굳이 한줄 출력 할 필요는 없지만 코드의 길이를 줄이고 싶기에..
print(f"{max(arr)}\n{arr.index(max(arr)) + 1}")