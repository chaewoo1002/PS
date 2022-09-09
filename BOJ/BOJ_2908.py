num1, num2 = input().split() # 한줄에 값을 입력받기 위해 .split() 사용, 역순으로 바꾸기 위해 int()는 사용 x
num1 = int(num1[::-1])       # num[::-1] 은 수를 역순으로 바꿔줌    ex) 751 -> 157
num2 = int(num2[::-1])

if num1 > num2:              # if num1이 num2보다 크다면
    print(num1)
else :                       # else 
    print(num2)