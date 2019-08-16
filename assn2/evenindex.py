inputval = raw_input ("Please eneter the input String\n")
def printevenindex(i):
    length = len(i)
    index = 0
    while(index < length):
        if (index%2==0):
            print (i[index]),
        index+=1
printevenindex(inputval)
