# Write a Python program to find duplicate letters between two strings.
# Example: In "virat" and "rohit", the duplicate letter is "r".

def duplicate(a):
    print(a)
    result=" "
    for char in a:
        if char not in result:
            result=result+char
        else:
            print(char)    
duplicate("viratrohit")            
        