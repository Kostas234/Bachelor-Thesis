def lcs_naive(x,y):
    
    length = len(x)
    z = []
    for i in range(length):
        for j in range(i,length):
            z.append(x[i:j+1])
    lcs=""
    lz=len(z)
    for i in range(lz-1):
        p=KMPSearch(z[i],y)
        if p>=0:
            if len(z[i])>len(lcs):
                lcs=z[i]
    return lcs
