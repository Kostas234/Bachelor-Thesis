# LCP(word by word for 2 words)

def LCP(x,y):
    
    result = ""
    n1=len(x)
    n2=len(y)
    if n1>n2:
        n=n2
    else:
        n=n1
    for i in range(n):
        if x[i]!=y[i]:
            break
        result += x[i]
        
    print result,
