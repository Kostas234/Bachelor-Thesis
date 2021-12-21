def lcs(x,y):
    
    n=len(x)
    m=len(y)
    result=""
    l3n=0
    row=0
    col=0
    L=[[0 for v in range(m)]for w in range(n)]
    
    for i in range(n):
        for j in range(m):
            if x[i]==y[j]:
                L[i][j]=L[i-1][j-1]+1
                if l3n<L[i][j]:
                    l3n=L[i][j]
                    row=i
                    col=j
    if l3n==0:
        print "no common substring"
    
    while L[row][col]!=0:
        result=x[row]+result
        row-=1
        col-=1
        
    return result
