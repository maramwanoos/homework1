infile=open("t.txt","r")
c=0
l=[line.rstrip() for line in infile]
for i in l:
    print(i[0:4])
    a=input("enter your answer")
    if a==i[-1]:
        c+=1
name=input("enter your name")
print(name,"answer a",c)
outfile=open("out.txt","w")
outfile.write(name+str(c))
outfile.close()
infile.close()
