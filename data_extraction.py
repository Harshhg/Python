f = open("myfile.txt","r")
temp=0
word=""
list=[]
for x in f:
    for y in x:
        if y!=',' and temp!=1:
            word+=y
        else:
            temp=1
        temp = 0 if y=='\n' else temp

    list.append(word)
    word=""
print(list)

