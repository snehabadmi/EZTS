n=[2,4,3,5,6,3,4,6,7,1,2,5]  
sum=max=0
for i in range(0,len(n)-2):
    sum=n[i]+n[i+1]+n[i+2]
    if max<sum: 
        max=sum
        pos=i
print(max,n[pos],n[pos+1],n[pos+2])