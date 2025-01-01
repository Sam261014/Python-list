n1=int(input("Enter no of elements in List1 "))
lst1=[0]*n1
for i in range(n1):
    print("Enter",i+1,"Numbers for list1:",end='')
    lst1[i]=int(input())

print("\nList:",end='')
for i in range(n1):
    print(lst1[i],end='')

p=int(input("Enter position"))
for i in range(pos-1,n1-1):
    lst1[i]=lst1[i+1]
lst.pop()

print("\nAfter Delete List:",end='')
for i in lst1:
    print(i,end='')
