x=eval(input("Enter list elements"))
print("Elements of list are",x)
for i in x:
    if i%2!=0:
        x.remove(i)
print("List after removing odd elements",x)
