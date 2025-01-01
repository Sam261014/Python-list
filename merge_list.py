def merge(x,y):
    z=[]
    Lst1=len(x)
    Lst2=len(y)
    i,j=0,0
    while i<Lst1 and j<Lst2:
        if x[1]<y[j]:
            z.append(x[i])
            i+=1
        elif y[j]<x[i]:
            z.append(y[j])
        else:
            i+=1
    while i<Lst1:
        z.append(x[i])
        i+=1
    while j<Lst2:
        z.append(y[j])
        j+=1
    return z

a=eval(input("Enter List 1 Element"))
b=eval(input("Enter List 2 Element"))
m=merge(a,b)
print("After merge:",m)
