lst = eval(input("Enter the list of elements: "))
n=len(lst)
if n%2==0:
    j=n//2
else:
    j=n//2+1
for i in range(n//2):
    lst[i],lst[j]=lst[j],lst[i]
    j+=1
print("\nAfter Shifting List Elements are:",end='')
for i in range(n):
    print(lst[i],end='')
