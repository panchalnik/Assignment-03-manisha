# Write a Python program to generate the pattern of the letter H.

for i in range(7):
    if i == 3:
        print("* " * 5)
    else:
        print("*       *")






n=7
for i in range(n):
    for j in range(n):
        if j==0 or j==n-1 or i==n//2:
            print("*", end=" ")  
        else:
            print(" ",end=" ")      

    print()          