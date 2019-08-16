list1 = [12,24,35,24,88,120,155,88,120,155]
newlist = []
dictc = {}
def dup_rem(list1):
    for i in list1:
        if not i in dictc.keys():
            dictc[i] = 0
    for k in dictc.keys():
        newlist.append(k)
    newlist.reverse()
    print (newlist)

dup_rem(list1)
