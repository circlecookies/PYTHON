a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
num = input("Input number: ")
new_list = []
for i in a:
    if i < num:
        new_list.append(i)

print a
print new_list
