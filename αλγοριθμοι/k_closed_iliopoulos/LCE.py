def LCE(x,i,j):
	n=len(x)
	length=0
	while x[i+length]==x[j+length]:
		length+=1
		if j+length==n:
			break        
	return length+1
