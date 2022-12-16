t = int(input())

if t%10 != 0:
    print(-1)
else:
    a = t//300;
    t = t%300;
    b = t//60;
    t = t%60;
    c = t//10;
    print(a, b, c)