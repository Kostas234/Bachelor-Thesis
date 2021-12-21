def computeLCS(master, subseq):
    """
	Wrapper method to compute the Longest Common Subsequence in an inputed master string given an inputed proposed subsequence string.
	Note that the length of the 'subseq' string parameter must be less than or equal to the length of the 'master' string parameter.
	
	This dynamic programming algorithm runs in O(n^2) time where n is the length of the 'master' string parameter.
	The total space required is O(n^2) due to the memoization step.
    """

    memoized = LCSLength(master, subseq)
    return "".join(LCSBackTrack(subseq, memoized))    


def LCSLength(master, subseq):
    """
	Returns a multi-dimensional list that contains the length of the Longest Common Subsequence (LCS).
	Note that the length of the 'subseq' string parameter must be less than or equal to the length of the 'master' string parameter.
    """       

    if len(subseq) > len(master):
       raise Exception("The length of the subsequence must be less than or equal to the length of the master string being tested")
    # Build a multi-dimensional list filled with 0s based on the inputed parameters
    memoized = [[0]*(min(len(master), len(subseq))+1) for i in range(max(len(master), len(subseq))+1)]        	

    # Populate the multi-dimensional list with the length of the longest common subsequence
    for masterIndex in range(len(master)):
        for subseqIndex in range(len(subseq)):	    
            if master[masterIndex] == subseq[subseqIndex]:
                memoized[masterIndex+1][subseqIndex+1] = memoized[masterIndex][subseqIndex] + 1
            else:
                memoized[masterIndex+1][subseqIndex+1] = max(memoized[masterIndex+1][subseqIndex], memoized[masterIndex][subseqIndex+1])

    return memoized

def LCSBackTrack(subseq, memoized):
    """
	Uses the multi-dimensional list containing the memoized LCS length values to construct a list containing the characters that make up 
	the LCS.	
    """

    lcs = []
    # Get the value in the bottom right hand corner of the inputed multi-dimensional list
    height = len(memoized)-1
    width = len(memoized[height])-1

    while height >= 0 and width >= 0 and memoized[height][width] != 0:
    	if memoized[height][width-1] != memoized[height][width]:
	   if memoized[height-1][width] != memoized[height][width]:
	      lcs.append(subseq[width-1])
	   height -= 1
	   continue
	width -= 1
	continue   
	
    lcs.reverse()
    return lcs
		      

