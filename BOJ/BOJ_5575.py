for i in range(3):
    sh, sm, ss, eh, em, es = map(int, input().split())
    start = (sh*3600)+(sm*60)+ss
    end = (eh*3600)+(em*60)+es
    t = end - start
    h = t//3600
    m = (t%3600)//60
    s = (t%3600)%60
    
    print(h, m, s)