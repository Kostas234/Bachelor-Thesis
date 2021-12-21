# LCP(word by word)
 
# lcp for 2 strings
def lcp(x,y):

    result = ""
    n=min(len(x),len(y))
    
    for j in range(n):
        if x[j]!=y[j]:
            break
        result += x[j]
         
    return result
 
def LCP(x):
     
    n=len(x)
    result=x[0]
    for i in xrange(1,n):
        result=lcp(result,x[i])
         
    return result           

