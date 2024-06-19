'''Bubble Sort'''
n=list(map(int,input("enter the numbers:").split()))
l=len(n)#convert list into integer
for i in range(0,l):#(0,4)
    for j in range(0,l-1-i):
        if n[i]>n[i+1]:
            n[i],n[i+1]=n[i+1],n[i]
print(n)
