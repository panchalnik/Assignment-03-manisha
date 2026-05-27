# Write a Python program to display all possible pairs of 3.
# Example: 1:3, 2:3, 3:3 , 2:1 , 2:2 ,2:3 , 3:1 ,3:2 ,3:3


def pairs(a):
    print(a)
    for i in range(1,4):
        print(f"{a}:{i}")
        i+=1
pairs(2)

