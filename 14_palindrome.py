# .Write a Python program to check whether a string entered by the user is a
# palindrome.

def palindrome(a):
    # pass
    print("The string is :",a)
    rev=" "
    i=len(a)-1
    while i>=0:
        rev=rev+a[i]
        print("The string is Palindrome:",rev)
        i-=1
    
        # print("The string is not Palindrome")    

palindrome("MADAM")
# print("If string is equal to rev, then it is a palindrome")