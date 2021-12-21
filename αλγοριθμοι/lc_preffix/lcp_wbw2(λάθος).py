# LCP(word by word)

def LCP(x):
    
    result=""
    result1 = ""
    n=len(x)
    if n==1:
        return x[0]
    else:
        result2=[""]*(n-1)
        j=0
        for i in range(n-1):
            if len(x[i])>len(x[i+1]):
                k=len(x[i+1])
            else:
                k=len(x[i])
            for j in range(k):
                if x[i][j]!=x[i+1][j]:
                    break            
                result1 += x[i][j]
                result2[i]=result1
            result1=""
        for m in range(n-2):
            if result2[m]>result2[m+1]:
                result=result2[m+1]
            else:
                result=result2[m]
        print result,
