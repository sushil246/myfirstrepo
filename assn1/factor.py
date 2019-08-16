number = input ("Enter The Number\n")
factoroddarray = []
factorevenarray = []
for i in range(1, number+1):
    if (number % i == 0):
        if (i % 2 == 0):
            factorevenarray.append (i)
        else:
            factoroddarray.append (i)
print ("Odd Factor", factoroddarray )
print ("Eeven Factor", factorevenarray )
