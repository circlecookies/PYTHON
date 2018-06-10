import random
a = []
a = random.sample(range(10),5)
def get_num(list_a):
    length=len(list_a)
    list_b=[]
    list_b.append(list_a[0])
    list_b.append(list_a[length-1])
    return (list_b)

print "List is:"
print a
x=get_num(a)
print "First and Last:"
print x
