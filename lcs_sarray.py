def lcs(x,y):
    
    s=x+"#"+y+"$"
    n=len(s)
    m=len(x)
    r=[]
    lcs=""
    p=1
    
    for i in range(n):
        r.append((s[i:n]+str('{0:05}'.format(p))))
        p+=1
        
    # lexikographiki taksinomisi tis listas    
    r=sorted(r) 
    for j in range(n-1):
        #print r[j][len(r[j])-5:len(r[j])]
        #rint r[j+1][len(r[j+1])-5:len(r[j+1])]
        l=LCP([r[j],r[j+1]])
        if len(l)>=len(lcs) and ((int(r[j][len(r[j])-5:len(r[j])])<(m+1) and int(r[j+1][len(r[j+1])-5:len(r[j+1])])>(m+1)) or (int(r[j][len(r[j])-5:len(r[j])])>(m+1) and int(r[j+1][len(r[j+1])-5:len(r[j+1])])<(m+1))):
            #print "-------------------------->skase","\n------------------------------>",r[j],"\n----------------------------->",r[j+1]
            lcs=l
        #print l
                
    return lcs
