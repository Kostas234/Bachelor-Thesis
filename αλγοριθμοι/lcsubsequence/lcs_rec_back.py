def lcs_recursive_backwards(A, B):

    # if one of either A or B is empty, this means that there is no possible common subsequence left
    if not A or not B:
        return 0

    # case 1 of the recursion: A and B end in the same value
    if A[-1] == B[-1]:
        return 1 + lcs_recursive_backwards(A[:-1], B[:-1])

    # case 2 of the recursion: they don't match, so we need to test deleting either one
    return max(
        lcs_recursive_backwards(A, B[:-1]),
        lcs_recursive_backwards(A[:-1], B))
