# LCSub Brute Force

def lcsub(x,y):
    
    if x=="" and y=="":
        print "Strings are empty"
        
    n=len(x)
    m=len(y)
    longest=0
    for i in range(n):
        for j in range(m):
            count=0
            while x[i+count]==y[j+count]:
                count+=1
                if i+count>=n or j+count>=m:
                    break
                elif count>longest:
                    longest=count
                    start=i
                    
    return x[start:start+longest+1]
