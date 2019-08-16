evenarray = []
for i in range (1000, 3000+1):
    count = 0
    stri = str(i)
    for x in stri:
        if (int(x)%2 == 0):
            count = count + 1
    if (count == len(stri)):
        evenarray.append(i)

print (evenarray)
