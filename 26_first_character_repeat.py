#Given: text = "knowyourself"
#Goal: Find and print the first character that repeats.

text="knowyourself"
repeat=""
for i in text:
    # print(i)
    if i not in repeat:
        repeat=repeat+i
        # print(repeat)
    else:
        print(i)    