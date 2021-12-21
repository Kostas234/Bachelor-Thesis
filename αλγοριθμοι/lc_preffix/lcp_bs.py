def LCP(x):
    
    n=len(x)    
    prefix=""
    m=len(x[0])
    for i in range(n-1):
        m=min(m,len(x[i+1]))
        
    low=0
    high=m
    mid=low+(high-low)/2
    
    for i in range(1,n):
        for j in range(mid):
            if x[i][j]!=x[0][j]:
                prefix=x[0][0:j]
                break
        else:
            prefix=x[0][0:mid]
            
            for w in range(1,n):
                for v in range(mid,high):
                    if x[w][v]!=x[0][v]:
                        prefix=x[0][0:v]
                        break
                else:
                    prefix=x[0][0:high]
                    continue
                break
            continue
        break
        
    return prefix
