num=input("Input a number: ")
new_list = []
i=1
while i < num:
    if num%i==0:
        new_list.append(i)
    i=i+1
print new_list
