# 참고 : https://yoonsang-it.tistory.com/49

import sys

n = int(sys.stdin.readline())
num_lst = [0] * 10001  # num_lst.append()를 사용할 수 없으므로 그냥 리스트를 10,001개 생성한다. 10,000개가 아닌 이유는
                        # 인덱스 값이 0부터 시작하므로 그냥 출력하기 편하게 10,001개 만들어야 한다고 한다

for _ in range(n):
    num_lst[int(sys.stdin.readline())] += 1    # 입력 받아서 num_ls내의 해당 인덱스 값에 1을 더한다

for i in range(10001):
    if num_lst[i] != 0:             # 0 ~ 10,001까지 인덱스를 찾아 0이 아닌 값의 경우,
        for j in range(num_lst[i]): # 그 인덱스 값의 수만큼 인덱스를 출력
            print(i)

# 아래 코드는 처음 풀었던 코드. 메모리초과로 인해 문제 해결 실패
    # 왜? 파이썬의 경우 for문 내에서 리스트명.append()를 사용할 경우 메모리 재할당이 일어나 메모리를 효율적으로 사용하지 못한다.
    # 일반적으로 값이 작을 경우 큰 문제는 없지만 입력값이 최대 10,000개로 주어진 이 문제에서는 위 방식으로 문제를 해결해야 한다

# import sys

# n = int(input())
# num_lst = []

# for _ in range(n):
#     num_lst.append(int(sys.stdin.readline()))

# num_lst.sort()

# for i in num_lst:
#     print(i)