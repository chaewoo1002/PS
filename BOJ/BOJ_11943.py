a, b = map(int, input().split()) # 첫번째 바구니에 있는 사과 a개, 오렌지 b개
c, d = map(int, input().split()) # 두번째 바구니에 있는 사과 c개, 오렌지 d개
                                 # 방법은 2가지다. 사과 a개와 오렌지 d개를 옮기기, 사과 c개와 오렌지 b개를 옮기기
                                 # 둘 중 더 작은 값을 출력한다.
print(min(a+d, b+c))