'''1.Find the vowels
2.count the occurance
3.sentence:-read it word by word'''
def count_vowel(sent):
    dic={'A':0,'E':0,'I':0,'O':0,'U':0}
    for i in sent:
        if i=='a'or i=='A':
            dic['A']+=1
        elif i=='e'or i=='E':
            dic['E']+=1
        elif i=='i'or i=='I':
            dic['I']+=1
        elif i=='o'or i=='O':
            dic['O']+=1
        elif i=='u'or i=='U':
            dic['U']+=1
    x=max(dic.values()) 
    result=[]
    for i,j in dic.items():
        if j==x:
            result.append(i)
    return result
i_p=[
    ["Alex","I enjoy hicking in the mountains."],
    ["sam","A lovely sunny day at beach."],
    ["Jamie","Reading a book is my favorit pastime."],
    ["Taylor","I love playing video game on weekends"],
    ["chirs","i am good boy"]
]
o_p={}
for i in i_p:
    o_p[i[0]]=count_vowel(i[1])
print(o_p)