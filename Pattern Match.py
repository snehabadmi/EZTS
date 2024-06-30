def Kmpalgo(p,S):
    m =len(p)
    N = len(S)
    lps=[]
    LPS(p,m,lps)
    print(lps)
    i=0
    j=0
    while(N-i) >= (m-j):
        if p[j] == S[i]:
            i+=1
            j+=1
        if j == m:
            print("pattern Found :",i-j)
            j=lps[j-1]
        elif i < N and p[j] != S[i]:
            if j != 0:
                j= lps[j-1]
            else:
                i+=1

def LPS(p,m,lps):
    lps.append(0)
    j=0
    for i in range(1,len(p)):
        if p[i]==p[j]:
            lps.append(j+1)
            j=j+1
        else:
            j=0
            lps.append(j-1)
if __name__=="__main__":
    S="ABABACDEABABABCABCABCABDAA"
    p = "ABCAB"
    Kmpalgo(p,S)