def sort2(val):
    return val[0]

inputwords = raw_input ("Enter the words to be sorted\n ")
arr = inputwords.strip().split(" ")
print(arr)
print(arr[0][1])
arr.sort(key = sort2)
print(arr)
