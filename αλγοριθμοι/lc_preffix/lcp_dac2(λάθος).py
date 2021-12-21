# LCP divide and conquer

# lcp2=LCP(for 2 strings)
def lcp2(x,y):
    
    result = ""
    #n1=len(x)
    #n2=len(y)
    #if n1>n2:
    #    n=n2
    #else:
    #   n=n1
    m=len(x[0])
    for i in range(n-1):
        if len(x[i+1])<m:
            m=len(x[i+1])
    for i in range(m):
        if x[i]!=y[i]:
            break
        result += x[i]
        
    return result
    
def LCP(x):

    n=len(x)
    g=0
    if n==1:
        return x[0]
    elif n%2==0:
        w=0
        while True:
            if n==2**w:
                break
            w+=1
        for v in range(w):
            for j in xrange(0,n,2):
                x[g]=lcp2(x[j],x[j+1])
                g+=1                    
                n=n/2
            g=0
        return x[0]
    
    else:
        if n%2==1:
            n=n-1
            a=x[n]
            w=0
            while True:
                if n==2**w:
                    break
                w+=1
            for v in range(w):
                for j in xrange(0,n,2):
                    x[g]=lcp2(x[j],x[j+1])
                    g+=1
                n=n/2
                g=0
        result=lcp2(x[0],a)
        return result         
        
