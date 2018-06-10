import random
num=10
while(num==10):
    x=0
    rand_num=random.randint(1,9)
    trials=0
    while x==0:
        your_num=input("input a number: ")
        if(your_num==rand_num):
            print "correct. You tried "+ str(trials) + " times"
            x=1
        elif(your_num==0):
            print "quitting. number is " + str(rand_num)
            num=0
            x=1
        elif(your_num<rand_num):
            print "your number is lower"
            trials=trials+1
        else:
            print "your number is higher"
            trials=trials+1

