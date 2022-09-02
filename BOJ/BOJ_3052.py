arr = []

arr = [(int(input()) % 42) for i in range(10)]

# set 메서드는 배열의 중복을 제거해줌
arr = set(arr)
# 위 set(list) 메서드를 사용해 배열의 중복을 제거하였으므로 배열의 길이 == 서로 같은 나머지를 제외한 나머지의 개수
print(len(arr))