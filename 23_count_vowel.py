# Given: text = "python programming"
# Goal: Count how many vowels are in the string.
# Constraint: Do not use indexing (text[i]) or slicing (text[:]).


def text(a):
    print(a)
    c=0
    for i in "aeiou":
        c+=1
    return c


res=text("python programming")  
print(res)  