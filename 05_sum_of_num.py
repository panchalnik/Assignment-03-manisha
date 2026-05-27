#  Write a Python program to calculate the sum of numbers between a starting and 
# ending point provided by the user.

start=int(input("Enter your Starting number:"))
end=int(input("Enter your last number :"))
sum=0
for i in range(start+1,end):
    sum=sum+i
    i+=1
    print(f"Adding the numbers between strings {start} and {end} is :",sum)


print("End of Program.......................")    
