list1= [1,3,6,78,35,55]
list2=  [12,24,35,24,88,120,155]
def intersection(l1, l2):
    locallist = []
    for i in list1:
        if i in list2:
            locallist.append(i)
    print locallist
    return locallist

intersection(list1,list2)
