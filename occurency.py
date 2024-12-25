print("THIS PROGRAMME WILL COUNT OCCURANCE OF EACH ELEMENT \n\n")

n=int(input("HOW MANY ELEMENTS YOU WANT IN YOUR LIST? "))
lst=[0]*n
for i in range(n):
    print("\n ENTER",i+1,"NUMBER",end='')
    lst[i]=int(input())
print("\n\n YOUR LIST LOOKS LIKE :- \n\t\t",lst)
print("\n\n COUNTING OCCURANCY...")

for i in range(n):
    c=0
    f=0
    m==lst[i]
    for j in range(i-1,-1,-1):
        if m==lst[j]:
            f=1
    if f==0:
        for k in range(n):
            if m==lst[k]:
                c=c+1
        print("\n\t * OCCURANCY OFF",m,"IS:-",c)
print("\n\n")
      
        

  
               
        
        
    
 


