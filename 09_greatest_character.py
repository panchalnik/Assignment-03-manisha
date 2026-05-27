# Write a Python program to find the greatest character from the string "python".
def greatest(a):
    print(a)
    greatest="a"
    for ch in a:
        if ch > greatest:
            greatest=ch
    print("The greatest character is:",greatest)

greatest("cmadkjfhijdkvnhjdfkchewioa")