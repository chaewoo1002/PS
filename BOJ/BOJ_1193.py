n = int(input())

lne = 0
end = 0

while n > end:
    lne += 1
    end += lne

dif = end - n
if lne%2 == 0:
    nmt = lne - dif
    dmt = dif + 1
else:
    nmt = dif + 1
    dmt = lne - dif

print(f"{nmt}/{lne}")