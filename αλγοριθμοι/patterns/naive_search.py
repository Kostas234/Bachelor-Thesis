# Naive Search
# briskei patterns pou tou dineis mesa 
# se duo arxeia

def naive_search(y, x, n, m):
    i = 0
    while i <= n - m:
        j = 0
        while j < m and x[j] == y[j + i]:
            j += 1
        if j == m:
                print 'y occurs in x at the position %d' % (i)
        i += 1
