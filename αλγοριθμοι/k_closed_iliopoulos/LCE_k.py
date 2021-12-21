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
