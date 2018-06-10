def reverse(word):
    x=''
    i=len(word)
    while i != 0:
        x += word[i-1]
        i=i-1
        print x
    return x

print "input a word: "
word=raw_input()

print word
print word[::-1]
print range(len(word))
if word == word[::-1]:
    print "same"
else:
    print "different"

z=reverse(word)
if z == word:
    print "same"
else:
    print "different"


    
