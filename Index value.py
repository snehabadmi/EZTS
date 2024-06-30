# Txt : ABABACDEABABABCABCABCABDAA
# Pat : ABCAB
S="ABABACDEABABABCABCABCABDAA"
p=input()
n=len(p)
index=[]
for i in range(len(S)):
    if S[i:i+n] == p:
        index.append(i)
print(index)