import re
emptylist=[]
addition=0
##hand=open('123.txt')
##for line in hand:
##    #line=line.strip()
##    line=line.replace(" ", "")
##    line = line.replace("\n", "")
##    #line=line.split()
##    print(line)
####    x=re.findall('[0-9]+',line)
####    if len(x) !=1: continue
####    addition=addition+float(x[-1])
####    emptylist.append(x)
####    print(x)
##print('addition',addition)
##print(line)
##line='1 234 :'
##x=re.findall('[0-9]+',line)
##print(x)
with open ("234.txt","r") as line:
    x=line.readlines()
    for seo in x:
        n=re.findall('[0-9]+',seo)
        if len(n) ==0: continue
        for add in n:
            addition=addition+int(add)
print(addition)
        #print('n',n)
        
    #print(x)
