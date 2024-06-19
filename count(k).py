l=[int(i) for i in input("enter the list elements:").split(',')]
sum=max=0
k=int(input("enter range:"))
for i in range(0,len(l)-k+1):   
    sum=0                      
    for j in range(0,k): 
        sum+=l[i+j]
        if max<sum:
            max=sum
            pos=i
print(max)
for j in range(0,k):
    print(l[pos+j])