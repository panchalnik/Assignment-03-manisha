#  Write a Python program to generate a table of a number provided by the user. 

a=int(input("Enter Your Number:"))
i=0
for i in range(0,11):
    print(f"{a} X {i}={a*i}")
    i+=1


print("Table of given number is ready............")