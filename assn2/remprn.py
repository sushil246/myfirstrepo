list1 = [12,24,35,24,88,120,155]
def rem_24(list1):
    for i in list1:
        if (i==24):
            list1.remove(i)

rem_24(list1)
print(list1)
