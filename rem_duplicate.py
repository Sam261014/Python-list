n = int(input("Enter the number of elements in the list: "))
lst = [0] * n
for i in range(n):
    lst[i] = int(input("Enter a number: "))
i=0
while i<n:
    x = lst[i]
    j = i+1
    while j < n:
        if x == lst[j]:
            for k in range(j, n - 1):
                lst[k] = lst[k + 1]
            n -= 1  
        else:
            j += 1
    i += 1
print("List after removing duplicates: ", end='')
for i in range(n):
    print(lst[i], end=' ')
