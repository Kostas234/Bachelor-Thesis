def lcs_recursive_forwards(A, B):
    if not A or not B:
        return 0

    if A[0] == B[0]:
        return 1 + lcs_recursive_forwards(A[1:], B[1:])

    return max(
        lcs_recursive_forwards(A, B[1:]),
        lcs_recursive_forwards(A[1:], B))
