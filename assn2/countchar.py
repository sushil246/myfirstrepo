dictc = {}
inp = raw_input ("Enetr the String for Char to be counted \n")
def charcount(inp):
    for i in inp:
        if i in dictc.keys():
            dictc[i] +=1
        else:
            dictc[i]= 1
    for k ,v in dictc.items():
        print (k , v)
    print(dictc)
charcount(inp)
