
inp1=int(input())
inp2=int(input())
problem_solved=0
remaing_time=240-inp2
for i in range(1,inp1+1):
    if (remaing_time>0 and remaing_time>5*i):
        remaing_time=remaing_time-5*i
        problem_solved+=1
print(problem_solved)

    