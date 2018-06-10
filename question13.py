def do_fibo(x):
    i=0
    temp=1
    list_a = [0]
    while i < x:
        num=list_a[i]+temp
        list_a.append(num)
        temp=list_a[i]
        i=i+1
        print num
    return list_a

num=input("Number of times: ")
new_list=do_fibo(num)
print new_list[1:]
