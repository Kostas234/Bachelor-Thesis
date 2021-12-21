# LCS Shift

def lcs(x, y):
    a=list(x)
    b=list(y)
    if a == [] or b == []:
        return []
 
    l = len(a) + len(b) - 1 
    sa = a + (len(b) - 1) * ['']
    sb = (len(a) - 1) * [''] + b
    longest = []
 
    for k in range(l):
        cur = []
 
        for c in range(l):
            if sa[c] != '' and sb[c] != '' and sa[c] == sb[c]:
                cur.append(sa[c])
            else:
                if len(cur) > len(longest):
                    longest = cur
                cur = []
 
        if len(cur) > len(longest):
            longest = cur
 
        if sa[len(sa) - 1] == '':
            # Shift 'a' to the right.
            sa = [''] + sa[: len(sa) - 1]
        else:
            # Shift 'b' to the left.
            sb = sb[1:] + ['']
 
    return ''.join(longest)
