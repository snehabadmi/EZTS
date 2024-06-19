num = int(input("Enter the number: "))
temp = 0
if num<1:
    temp = 1
elif num == 1:
    temp = 0
else:
    for i in range(2,(num//2)+1):
        if num%i == 0:
            temp = 1
            break
    
if temp == 0:
    print("prime number")
else:
    print("not a prime number")
    