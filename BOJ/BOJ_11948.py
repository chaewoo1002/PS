list = [] 

for _ in range(6):  
    list.append(int(input())) 

list1 = sorted(list[:4]) 
list2 = sorted(list[4:]) 

print(sum(list1[1:]) + list2[-1])