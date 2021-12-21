# LCP(character by character)
 
def LCP(x):
   
	result=''
	n=len(x)
	m=len(x[0])
	for i in range(n-1):
		m=min(m,len(x[i+1]))
 
	for j in range(m):
		y=x[0][j]
		for k in range(n): 
			if x[k][j]!=y:
                		break
		else:
			continue
		break

	result += x[0][0:j+1] 

	return result
