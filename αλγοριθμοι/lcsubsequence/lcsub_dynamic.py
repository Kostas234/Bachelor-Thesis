# LCSub_dynamic

def lcs(x,y):
    
    n=len(x)
    m=len(y)
    L=[[0 for v in range(m+1)]for w in range(n+1)]
    #print L
    for i in range(n+1):
        for j in range(m+1):
            if i==0 or j==0:
                L[i][j]=0
            
            elif x[i-1]==y[j-1]:
                L[i][j]=L[i-1][j-1]+1
                
            else:
                L[i][j]=max(L[i-1][j], L[i][j-1])
             
    lcs=[""]
    i=n
    j=m
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            lcs.append(x[i-1])
            i-=1
            j-=1
        elif L[i-1][j]>L[i][j-1]:
            i-=1
        else:
            j-=1
        
    return "".join(reversed(lcs)) 
