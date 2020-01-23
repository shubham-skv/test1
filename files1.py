fname=open(input("enter file name"))
list1=[]
for line in fh:
    line=line.rstrip()
    l=line.split(' ')
    for i in l:
        if(i not in list1):
            list1.append(i)
print(list1)
    
