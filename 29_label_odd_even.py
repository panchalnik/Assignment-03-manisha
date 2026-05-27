# Take two numbers from the user: start and end. Print a string labeling each
# number in that range as Odd or Even.
# Output_format : 3:Odd 4:Even 5:Odd 6:Even 7:Odd 8:Even 9:Odd



start=int(input("Enter your starting number:"))
end=int(input("Enter your ending number:"))
for i in range(start+1,end-1):
    # print(i)
    if i%2==0:
        print(i,"is Even")
    else:
        print(i,"is odd")    
