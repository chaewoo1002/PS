# 2751번 문제와 거의 동일한 문제인듯 하다. 유일하게 다른 점이 있다면 리스트 내에 주어지는 값이 2751번의 경우 1 ~ 10000까지 값이 주어져
# sys.stdin.readline()을 사용해 풀어야하지만 2750번은 1000까지만 입력받으므로 굳이 그렇게 풀 필요가 없다. sys.stdin.readline()을 사용하는 이유는
# BOJ_2751.py 파일을 확인해보도록 하자

n = int(input())    # 입력받을 숫자의 개수 

num_lst = []    # 리스트명.append()를 사용하기 위해 빈 리스트를 생성
for _ in range(n):
    num_lst.append(int(input()))

num_lst.sort()  # 배열을 오름차순으로 정렬해줌

for i in num_lst:
    print(i)    # 배열 값 한줄씩 줄바꿈하며 출력