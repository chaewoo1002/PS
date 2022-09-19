import sys  # sys.stdin.readline()메서드 사용을 위한 sys 헤더파일을 포함

n = int(input())    # 입력받을 숫자의 개수 
num_lst = []    # 리스트명.append()를 사용하기 위해 빈 리스트를 생성
for _ in range(n):
    num_lst.append(int(sys.stdin.readline()))   # 기존 코드에서 input()을 사용했었지만 시간초과 발생, 왜?
                                                    # ㄴ>input은 sys.stdin.readline()에 비해 개행를 제거한 후 출력,
                                                    # prompt message를 삭제 한 후 리턴하기 때문에 반복문 내에서 사용하기에 부적합하다.

num_lst.sort()  # 배열을 오름차순으로 정렬해줌

for i in num_lst:
    print(i)    # 배열 값 한줄씩 줄바꿈하며 출력

# n = int(input())
# num_lst = []

# for i in range(0, n):
#     num_lst.append(int(input()))

# set(num_lst)
# num_lst.sort()

# for i in num_lst:
#     print(i)