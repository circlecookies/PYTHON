import random
xinp=1
i=1
while i != 0:
    pcinp=random.randint(1,3) #1 rock 2 paper 3 scissors
    xinp=10
    while (xinp == 10):
        print "rock, paper, scissors? type 0 to quit\n"
        rps=raw_input()
        enemy=random.randint(1,3)
        if rps =="rock":
            xinp=1
        elif rps=="paper":
            xinp=2
        elif rps=="scissors":
            xinp=3
        elif rps=="0":
            xinp=0
            i=0
        else:
            print "invalid input. please input again."
    print pcinp
    if pcinp==1:
        print "pc: rock"
    elif pcinp==2:
        print "pc: paper"
    else:
        print "pc: scissors"
    if xinp == pcinp:
        print "tie"
    elif xinp==1:
        if pcinp==2:
            print "pc wins"
        else:
            print "you win"
    elif xinp==2:
        if pcinp==1:
            print "you win"
        else:
            print "pc wins"
    elif xinp==3:
        if pcinp==1:
            print "pc wins"
        else:
            print "you win"
        
