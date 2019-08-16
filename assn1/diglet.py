string = raw_input("Enter the String ")
charcount = 0
digitcount = 0
for i in string:
    print (i)
    if (i.isdigit()):
        digitcount = digitcount+1
    if (i.isalpha()):
        charcount = charcount+1

print ("Characters in input string is ", charcount)
print ("Numbers in input string is ", digitcount)

'''
    count = 0
    stri = str(i)
    for x in stri:
        if (int(x)%2 == 0):
            count = count + 1
    if (count == len(stri)):
        evenarray.append(i)

print (evenarray)
'''
