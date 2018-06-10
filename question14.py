import random
a = [4, 14, 12, 15, 16, 2, 10, 9, 13, 19] ##random.sample(range(20),10)
b = [4, 4, 4, 15, 16, 2, 10, 9, 13, 19] ##random.sample(range(20),13)
new_list = [i for i in a for x in b if i==x]
print a
print b
print new_list
new_list = set(new_list)
new_list = list(new_list)
print new_list

