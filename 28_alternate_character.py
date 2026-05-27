# Given: text = "knowyourself"
# Goal: Find and print the alternate characters.


text="knowyourself"
b=len(text)
for i in range(0,b,2):
    print(i,text[i]," ",end=" ")