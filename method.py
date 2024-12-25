n=int(input("Enter no of Elements"))
Lst=[0]*n
for i in range(n):
    print("Enter",i+1,"Number:-",end='')
    Lst[i]=int(input())
print("List Elements are:",end='')
print(Lst)
