#  Write a Python program to print all odd and even numbers from 1 to 20.

a=1
for a in range(1,21):
    if a%2==0:
        print(a,"is even")
        a+=1
    else:
        print(a,"is odd")    