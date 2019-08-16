list1 = [12,24,35,70,88,120,155]
list2 = []
print(list1)

def remov_5_7(list1):
    for i in list1:
        list2.append(i)
    for i in list2:
        if ((i%5 == 0) or (i%7==0)):
            list1.remove(i)
            print list1

remov_5_7(list1)
