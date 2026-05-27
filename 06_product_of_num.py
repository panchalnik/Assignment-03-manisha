#Write a Python program to calculate the product of numbers between a starting 
#and ending point provided by the user. 

a=int(input("Enter your Starting Number:"))
b=int(input("Enter Your last number:"))
prod=1
for i in range(a+1,b):
    prod=prod*i
    i+=1
    print("The product is",prod)

print("Program ends here................")    