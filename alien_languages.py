import itertools
f = open('in', 'r')
n = f.readline()
n = int(n)
#print n

for line in f.readlines():
    #print line
    a = line.split(" ")
    num_letters = int(a[0])
    word_length = int(a[1])
    str = 'abcdefghijklmnopqrstuvwxyz'
    letters = str[0:num_letters]
    #print "letters "+letters
    alist = list(itertools.product(letters, repeat=word_length))
    count = 0
    for word in alist:
        for x in word:
            k = letters.index(x)
            print "k   === "+format(k)
            if (2*k) < num_letters:
                l = letters.index(word[k+1])
                
                if(2*l) < num_letters:
                    print "This cannot be added "+format(word)
                    break
                else:
                    last = word[(len(word)-1)]
                    i = letters.index(last)
                    i = i+1
                    if (2*i) > num_letters:
                        count = count+1
        
    print count