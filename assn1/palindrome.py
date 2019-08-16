def reverse (s):
    return s[::-1]

def isPalindrome(s,r):
    if (s==r):
        return True
    else:
        return False

istring = raw_input ("Enter the String \n")
if (isPalindrome(istring, reverse(istring))):
    print ("Its the palindrome string")
else:
    print ("its not palindrome")
