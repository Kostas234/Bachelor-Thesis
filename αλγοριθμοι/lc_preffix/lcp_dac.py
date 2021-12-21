# LCP divide and conquer

def lcp2(x,y):
    
    result = ""
    n=min(len(x),len(y))

    for j in range(n):
        if x[j]!=y[j]:
            break
        result += x[j]
        
    return result

def LCP(x,low,high):
    
    if low==high:
        return x[low]
    
    if high>low:
        mid=low+(high-low)/2
        
        str1=LCP(x,low,mid)
        str2=LCP(x,mid+1,high)
        
        result=lcp2(str1,str2)
        
        return result

    
