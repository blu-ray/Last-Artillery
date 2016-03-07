import random
    stlen=len(string)
    dstring=''
    pointer=0
    spot=key2%7
    while pointer<stlen :
        if not((pointer%spot==0) or (pointer%(13-spot)==0)):
            dstring=dstring+hdstring[pointer]
        pointer+=1
        
    return dstring
           
