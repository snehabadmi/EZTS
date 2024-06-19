def check_prime(m):
    flag=0  #because to find the next smallest prime number limit
    if m<1:
        flag=1
    elif m==1:
        flag=0
    else:
        for i in range(2,(m//2)+1):
            if m%i==0:
                flag=1
                break
    if(flag==0):
        return 1
    else:
        return 0  
result=[]    
N=int(input("enter number: "))
flag=0
k=N+1 #next prime number
while flag<1:  #we don't have upper limit so use while loop()
    flag=check_prime(k)
    if flag==1:
        result.append(k)
    else:
        k=k+1
        
        
        
#Sum of numbers between prime number k and it's next prime number of k

sum=0
for i in range(N+1,k):
    sum+=i
result.append(sum)

#to get next prime number of the smallest prime  number p1 i.e(N-->p1--->p2)
p1=k
flag=0
k=p1+1
while flag<1:
    flag=check_prime(k)
    if flag==1:
        p2=k
    else:
        k=k+1
        
        
        
#check the product of k and k+1 prime numbers is prime number or not

p3=p1*p2
flag=check_prime(p3)
if flag==0:
    result.append(False)
else:
    result.append(True)
prime_key=tuple(result)  #convert list into tuple
print(prime_key)