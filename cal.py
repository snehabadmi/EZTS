num=input()
ope=['+','-','*','/']
for i in num:
    if i in ope:
        x=i
        s=num.replace(x," ")

l=list(map(float,num.split()))

match x:
    case '+': print(l[0]+l[1])
    case '-': print(l[0]-l[1])
    case '*': print(l[0]*l[1])
    case '/': print(l[0]/l[1])
    case _ : print("Invalid Operator")
