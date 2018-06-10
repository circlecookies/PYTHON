print "Input a sentence:"
sentence=raw_input()
split_sent=sentence.split(' ')
print split_sent
reverse=[]
i=len(split_sent)
while i > 0:
    word = split_sent[i-1]
    reverse.append(word)
    i=i-1
reverse_j = " ".join(reverse)
print reverse_j
