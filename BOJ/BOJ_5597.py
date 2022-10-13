import sys
stuid_lst = [i for i in range(1,31)]

for _ in range(28): # 총 28개의 값 입력
  stuid_lst.remove(int(sys.stdin.readline()))

print(*stuid_lst, sep = "\n") # 가변인자 사용, sep = ""을 사용하면 문자열 출력에 구분자를 포함할 수 있다.