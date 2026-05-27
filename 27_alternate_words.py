# Give : text=”if you think you can not do, you can not show think wisely”
# Goal: Print the alternate words
# Constraint: Do not use space between words more than once

text ="if you think you can not do,you can not show think wisely"
b=len(text)
for i in range(1,b,2):
    print(i,text[i],"",end=" ")