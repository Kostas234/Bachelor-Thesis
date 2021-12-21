def lcs_recursive_backwards_indices(A, B, i = 0, j = 0):
    if i >= len(A) or j >= len(B):
        return 0

    elif A[i] == B[j]:
        return 1 + lcs_recursive_backwards_indices(A, B, i+1, j+1)

    return max(
        lcs_recursive_backwards_indices(A, B, i, j+1),
        lcs_recursive_backwards_indices(A, B, i+1, j))
