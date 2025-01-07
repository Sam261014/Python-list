n=int(input("Enter no of elements"))
lst=[]
for i in range(n):
    print("Enter",i+1,"Number:",end='')
    a=int(input())
    lst.append(a)
print("List elements are:", end='')
print(lst)
for i in range(0,n,2):
    if i>=n-1:
        break
    lst[i],lst[i+1]=lst[i+1], lst[i]

print("After update list elements are:")
print(lst)
