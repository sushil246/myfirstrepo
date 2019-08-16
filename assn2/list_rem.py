list1 = [12,24,35,24,88,120,155]
index1 = [0, 4, 5]
print(list1)
print(index1)
def rem_24(index):
    count = 0
    for i in index:
        print ("index is ", i)
        del list1[i-count]
        count +=1

rem_24(index1)
print(list1)
