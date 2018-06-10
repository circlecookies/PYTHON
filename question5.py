import random
a=random.sample(range(1,100),10)
b=random.sample(range(1,100),10)
#a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
new_list = []
for i in a:
    for x in b:
        if i == x:
            new_list.append(i)
print a
print b
print new_list
