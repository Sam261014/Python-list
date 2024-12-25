lst=eval(input("Enter elements of list"))
print(lst)
f1,f2=0,0
for i in range(len(lst)):
        if lst[i]<=lst[i+1]:
            f1+=1
        if lst[i]>=lst[i+1]:
            f2+=1

if f1==len(lst)-1:
    print("ASC")
elif f2==len(lst)-1:
    print("DESC")
else:
    print("unordered")

        
    
