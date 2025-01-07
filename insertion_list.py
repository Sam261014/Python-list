n=int(input("Enter no for elements in list1"))
lst1=[0]*(n+1)

for i in range(n):
    print("Enter",i+1,"Number for List 1:",end='')
    lst1[i]=int(input())
print("\nList:", end='')
for i in range(n):
    print(lst1[i],end='')
ch=1
while ch!=0:
    x=int(input("\nEnter no for insertion"))
    pos=int(input("\nEnter position"))

    for i in range(n,pos-1,-1):
        lst1[i]=lst1[i-1]
    lst1[pos-1]=x
    n=n+1
    print("List Now :",lst1)
    ch=int(input("Do you want another insertion(0->No,1->Yes)"))
    if ch==1:
        lst1.append(0)
    
