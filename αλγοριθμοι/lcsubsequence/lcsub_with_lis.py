class LIS():

def lis(x):
    
    n=len(x)
    y=[""]
    l=[]
    y[0]=x[0]
    for i in range(n-1):
        k=len(y)
        if len(y)==1 and x[i+1]<y[0]:
            l.extend([y[0],x[i+1]])
            y[0]=x[i+1]
        elif x[i+1]>y[k-1]:
            y.extend([x[i+1]])
            l.extend([y[k-1],x[i+1]])
        elif x[i+1]<y[k-1] and len(y)>1:
            for j in range(k):
                if x[i+1]<y[j]:
                    if j==0:
                        l.extend([y[j],x[i+1]])
                    else:
                        l.extend([y[j-1],x[i+1]])
                    y[j]=x[i+1]
                    break
                elif j==k-1:
                    l.extend([y[0],x[i+1]])
                    y[0]=x[i+1]
    
    s=[]
    s.append(y[len(y)-1])
    for g in range(len(y)-1):
        for f in range(len(l),0,-1):
            if f%2==1 and l[f]==s[0]:
                s.insert(0,l[f-1])
                break
         
    print "Mikos LIS:",len(y),"\n","LIS:",s

def lcsub(x,y):
    
    n=len(x)
    m=len(y)
    pA=[]
    pC=[]
    pG=[]
    pT=[]
    s=[]
    
    for i in range(m-1,-1,-1):
        if y[i]=="A":
            pA.append(str(i+1))
        elif y[i]=="C":
            pC.append(str(i+1))
        elif y[i]=="G":
            pG.append(str(i+1))
        elif y[i]=="T":
            pT.append(str(i+1))
            
    for j in range(n):
        if x[j]=="A": 
            s.append(''.join(pA))
        elif x[j]=="C":
            s.append(''.join(pC))
        elif x[j]=="G":
            s.append(''.join(pG))
        elif x[j]=="T":
            s.append(''.join(pT))
    s=''.join(s)
    f=[]
    for w in range(len(s)):
        p=0
        for g in range(w,len(s)):
            if s[w]==s[g]:
                p+=1
            if g==len(s)-1:
                f.append([int(s[w]),p])
    
    f2=sorted(f)
    
    for u in range(len(f2),0,-1):
        f2[u-1].append(u)
    
    for z in range(len(f)):
        f[z]=f[z][2]
        
    return lis(f)
