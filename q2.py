def dec2bin():   
    m=int(input("enter num to convert: "))
    l=[]
    while m>0:
        r=m%2
        l.append(r)
        l.reverse()
        m=m//2
    for i in l:
        print(i,end="")

dec2bin()
