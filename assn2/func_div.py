num = input ("Enter the number to conpute formula 0+1/1+1...n/n+1\n")
def compute_num(n):
    output = 0
    list1= xrange(1,n+1)
    for i in list1:
        output = output + (float (i)/float (i+1))
    return output
print(compute_num(num))
