lst=[]
n=int(input("Enter no of Elements"))
for i in range(1,n+1):
    print("Enter",i,"Number:",end='')
    a=int(input())
    lst.append(a)
print(lst)
print("List Elements are",end='')
for i in range(n):
    print(lst[i],end='')
          
