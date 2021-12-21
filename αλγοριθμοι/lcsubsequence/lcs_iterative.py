def lcs_iterative(A, B, i, j):

    def empty_list():
        return [0] * (len(B)+1)

    K = [empty_list() for temp in range(len(A)+1)]
    for i in range(len(A)-1,-1,-1):
        for j in range(len(B)-1,-1,-1):
            if A[i] == B[j]:
                K[i][j] = 1+K[i+1][j+1]

            else:
                K[i][j] = max(K[i][j+1], K[i+1][j])

    return K[0][0]
