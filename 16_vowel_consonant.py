# Write a Python program to filter out all vowels and consonants from a string
# entered by the user

def str(a):
    print(a)
    for i in a:
        if i in "aeiouAEIOU":
           print(i,"is vowel")
        else:
            print(i,"is consonant")
        
str("Manisha Panchal")  