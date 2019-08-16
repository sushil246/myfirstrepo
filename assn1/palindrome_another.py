def isPalindrome(s):
    length = len(s)
    for i in range(0,len(s)/2):
        if (s[i]==s[length-i-1]):
            return True
        else:
            return False

istring = raw_input ("Enter the String \n")
if (isPalindrome(istring)):
    print ("Its the palindrome string")
else:
    print ("its not palindrome")
