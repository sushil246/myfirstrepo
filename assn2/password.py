password = raw_input("Please enter the Password to contunue \n")
def passwordvalidation(passwd):
    char=False
    capchar=False
    integer=False
    special=False
    length = len (passwd)
    if (length >= 6 and length <=12):
        for i in passwd:
            print (i)
            if (i>="a" and i<="z"):
                char = True
            elif (i>="A" and i<="Z"):
                capchar = True
            elif ((i=="$") or (i=="@") or (i=="#")):
                special = True
            elif((i>="0") and (i<="9")) :
                integer = True
    if (capchar and char and special and integer):
        return True

if (passwordvalidation(password) == True):
    print("Entered Password is fine")
else:
    print("Entered Password is not good")
