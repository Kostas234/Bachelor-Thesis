def lcs_iterative_with_sequence(A, B, i, j):

    def empty_list():
        return [0] * (len(B)+1)

    # Step 1: build lookup array to determine LCS
    K = [empty_list() for temp in range(len(A)+1)]
    for i in range(len(A)-1,-1,-1):
        for j in range(len(B)-1,-1,-1):
            if A[i] == B[j]:
                K[i][j] = 1+K[i+1][j+1]

            else:
                K[i][j] = max(K[i][j+1], K[i+1][j])

    # Step 2: restore sequence from information in lookup array
    S = []
    i = 0
    j = 0
    while (i < len(A)) and (j < len(B)):
        if A[i] == B[j]:
            S.append(A[i])
            i += 1
            j += 1
        elif K[i+1][j] >= K[i][j+1]:
            i += 1

        else:
            j += 1
    return S
