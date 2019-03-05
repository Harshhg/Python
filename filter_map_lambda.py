
ts = 0
def even_odd(x,flag=1):
        if(x%2==0):
            return False
        else:
            return True
def sum(x):
    global ts
    ts+=x
    return ts



mylist = [1,2,3,4,5,6,7,8,9,10]
odd_list = filter(even_odd,mylist)
even_list = filter(lambda x :  (x%2==0), mylist)
sum_of_all = map(sum,mylist)

ol= []
nl=[]
sl = []
for x in odd_list:
    ol.append(x)
for x in even_list:
    nl.append(x)
for x in sum_of_all:
    sl.append(x)
print("Odd list", ol)
print("Even List" , nl)
print("Sum of all" , sl)
