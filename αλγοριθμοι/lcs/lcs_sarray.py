def lcs(x,y):
    
    s=x+"#"+y+"$"
    n=len(s)
    r1=[]
    lcs=""
    
    for i in range(n):
        r1.append(s[i:n])
    r1=sorted(r1) # lexikogragikh taksinomhsh ths listas
    
    for j in range(n-1):
        l=LCP([r1[j],r1[j+1]])
        if len(l)>len(lcs):
               lcs=l
                
    return lcs
