#LCSub Naive

def lcs_n(x,y):
    
    n=len(x)
    m=len(y)
    
    if n==0 or m==0:
        return ""
    
    if x[n-1]==y[m-1]:
        return lcs_n(x[0:n-1],y[0:m-1])+x[n-1]
    
    l1=lcs_n(x,y[0:m-1])
    l2=lcs_n(x[0:n-1],y)
    
    if len(l1)>len(l2):
        return l1
    else:
        return l2
