#  Write a Python program to check if a number provided by the user is prime or not. 


a=int(input("Enter your number :"))
if a>1:
    for i in range(2,a):
        if a % i==0:
            print(a,"Number is Not Prime")
            break
        else:
            print(a,"Number is Prime")

else:
    print(f"The Prime Number starts from 2 and {a} is less than 2")    



# num = int(input("Enter a number: "))

# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print(num, "is not a Prime Number")
#             break
#     else:
#         print(num, "is a Prime Number")
# else:
#     print(num, "is not a Prime Number")