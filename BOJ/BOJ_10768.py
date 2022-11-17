month = int(input())
day = int(input())
if month == 2 and day == 18:
    print('Special')
elif month == 2:
  print('After' if day > 18 else 'Before')
elif month > 2:
    print('After')
elif month < 2:
    print('Before')