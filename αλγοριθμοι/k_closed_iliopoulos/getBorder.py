# k_closed

import numpy as np

def LCE_k(x,i,j,k):
    p=0
    n=len(x)
    length=0
    while True:
        if x[i+length]==x[j+length]:
                length+=1
        else: 
            p+=1
            if p==k+1:
                break
            length+=1
            
        if j+length==n:
            break
        
    return length

def Reverse(x):
    x_l=list(x)
    x_l.reverse()
    x_rl=x_l
    x_r=''.join(x_rl)
    
    return x_r

def LPM(x,k):
    l=len(x)
    
    lpm=np.arange(l)
    for i in range(l):
        lpm[i]=-1
        
    for j in range(l):
        if j==0:
            lpm[j]=-1
        else: lpm[j]=LCE_k(x,0,j,k)
    
    return lpm

def LSM(x,k):
    
    l=len(x)
    
    lsm=np.arange(l)    
    for i in range(l):
        lsm[i]=-1
        
    x=Reverse(x)
    for j in range(l):
        if j==l-1:
            lsm[j]=-1
        else: lsm[j]=LCE_k(x,0,l-1-j,k)
            
    return lsm

def getBorder(x,k):
    
    n=len(x)
    m=0
    c=0
    con1=np.arange(n)
    con2=np.arange(n)
    con3=np.arange(n)
    con=np.arange(n)
    
    for i in range(n):
        con1[i]=0
        con2[i]=0
        con3[i]=0
        con[i]=0
        
    lpm=LPM(x,k)
    lsm=LSM(x,k)
    
    for j in range(n):
        r=0
        p=0
        # first condition
        if j+lpm[j]==n:
            con1[j]=1
        # second condition
        if j==0:
            con2[j]=1
        else:
            for m in range(j):
                if lpm[j]>lpm[m]:
                    r+=1
                    if r==j:
                        con2[j]=1
        # third condition
        if j==0:
            con3[j]=1
        else:
            for c in range(j):
                if lsm[n-j-1]>lsm[n-c-1]:
                    p+=1
                    if p==j:
                        con3[j]=1
    
    
    for s in range(n-1):
        con[s]=con1[s]*con2[s]*con3[s]
        if con[s]==1:
            thesi=s
            mikos=n-thesi

    #return con
    print k,"closed-Border bre8ike sti 8esi",thesi,"kai exei mikos",mikos
