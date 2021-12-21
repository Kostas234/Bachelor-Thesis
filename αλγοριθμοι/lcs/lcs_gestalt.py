# SequenceMatcher apo th difflib, 
# gestalt approach pattern matching

from difflib import SequenceMatcher

def lcs_gestalt(A,B):

	match=SequenceMatcher(None,A,B).find_longest_match(0, len(A), 		0, len(B))

	

	print(match)
	print(A[match.a: match.a + match.size])
	print(B[match.b: match.b + match.size])

	return
