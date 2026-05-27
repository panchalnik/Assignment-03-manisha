# Write a Python program to filter out duplicate characters from a string entered by
# the user.

def duplicates(text):
    result = ""

    for char in text:
        print(char)
        if char not in result:
            result=result+ char

    return result
res=duplicates("manisha")
print(res)

# duplicates("manisha")