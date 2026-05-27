# Given: text = "programming"
# Goal: Print all characters that repeat in the string

def char(text):
    print(text)
    rev=" "
    for i in text:
        # print(i)
        if i not in rev:
            rev=rev+i
        else:
            print(i)    
      


char("programming")
