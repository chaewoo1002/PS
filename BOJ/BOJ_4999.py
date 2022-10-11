jaehwan = input() # 재환이가 낼 수 있는 소리의 길이
doc = input() # 의사가 요구하는 길이

if len(jaehwan) >= len(doc): # 재환이가 낼 수 있는 소리가 의사의 요구보다 길다면
  print("go")
else:
  print("no")