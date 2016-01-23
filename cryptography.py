import random
def make_chr_list():
    chrlist=''
    for i in range(33,127):
        if i != 92 and i!= 47:
            chrlist=chrlist+(chr(i))
    return chrlist

def encrypt(string,key1,key2):
    estring=''
    chrlist=make_chr_list()

    stlen=len(string)
    pointer=0
    spot=key2%7
    while pointer<stlen :
        if (pointer%spot==0) or (pointer%(13-spot)==0):
            string=string[:pointer]+chrlist[random.randrange(0,len(chrlist))]+string[pointer:]
        pointer+=1
        stlen=len(string)

    pointer=0
    for i in string:
        mychr=chrlist[(chrlist.find(i) + chrlist.find(key1[pointer]))% len(chrlist)]
        estring = estring + mychr
        pointer+=1
        if pointer>=len(key1) :
            pointer=0
        
    return estring
    
        

def decrypt(string,key1,key2):
    hdstring=''
    pointer=0
    chrlist=make_chr_list()
    for i in string :
        mychr= chrlist[(chrlist.find(i) - chrlist.find(key1[pointer])+len(chrlist))% len(chrlist)]
        hdstring = hdstring + mychr
        pointer+=1
        if pointer>=len(key1) :
            pointer=0

    stlen=len(string)
    dstring=''
    pointer=0
    spot=key2%7
    while pointer<stlen :
        if not((pointer%spot==0) or (pointer%(13-spot)==0)):
            dstring=dstring+hdstring[pointer]
        pointer+=1
        
    return dstring
           
