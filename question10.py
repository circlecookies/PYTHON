import random 
b = []
a = random.sample(range(1,11), 10)
c = random.sample(range(100), 10)
for i in range(0,9):
    x=random.randint(0,9)
    print x
    b.append(x)

print b
print a
print c
new_list = [i for i in c for num in a if i == num]
print new_list

result = []
for i in new_list:
    if i not in result:
        result.append(i)

print result
