# Write a Python program to display all letters except 'm' and 'i' from the string
# "Dreamer infotech".


def string(a):
    # pass
    # print(a)
    for i in a:
        # print(i)
        if i=="m" or i=="i":
            continue
        else:
            print(i)
        

        

res=string("Dreamer infotech")
print(res)