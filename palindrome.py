import sys

#using slicing of string

def reverse(string):

    if len(string) == 0:
        print("no string detected")

    return string[::-1] # time complexity O(n)


#s = sys.argv[1]

#if s == reverse(s):
#    print("Its a palindrome")

#else:
#    print("Its not")

#using algorithm
def isPalindrome(s):
    for i in range(0, int(len(s)/2)):
        if s[i] != s[len(s)-i-1]:
            return False
        return True

#print(isPalindrome(s))

#recursive solution
 
def recursivePalindrome(s):
    if len(s) <=1:
        return True
    else:
        return s[0] == s[-1] and recursivePalindrome(s[1:-1])


print(recursivePalindrome("anna"))
print(recursivePalindrome("bruh"))
print(recursivePalindrome("jesus"))